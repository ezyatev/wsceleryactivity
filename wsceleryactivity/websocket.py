#!/usr/bin/env python3

import logging
import re
from functools import partial

import tornado.websocket
from tornado import ioloop
from tornado.escape import json_encode

logger = logging.getLogger(__name__)


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    listeners = []
    periodic_callback = None
    update_interval = 1000

    def initialize(self, allow_origin=None):
        self.allow_origin = allow_origin

    def check_origin(self, origin):
        if not self.allow_origin:
            return super().check_origin(origin)
        match = re.match(self.allow_origin, origin)
        return match is not None

    def open(self):
        capp = self.application.capp

        if not self.listeners:
            if self.periodic_callback is None:
                cls = WebSocketHandler
                cls.periodic_callback = ioloop.PeriodicCallback(
                    partial(cls.on_update_time, capp),
                    self.update_interval)
            if not self.periodic_callback._running:
                logger.debug('Starting a timer for updates')
                self.periodic_callback.start()
        self.listeners.append(self)

    @classmethod
    def on_update_time(cls, capp):
        update = json_encode(cls.get_active_tasks(capp))
        if update:
            for l in cls.listeners:
                l.write_message(update)

    @staticmethod
    def get_active_tasks(capp):
        unique_tasks = set()
        active_tasks = capp.control.inspect().active()
        if not active_tasks:
            return []
        for worker, tasks in active_tasks.items():
            for task in tasks:
                unique_tasks.add(task['name'])
        return list(unique_tasks)

    def on_message(self, message):
        pass

    def on_close(self):
        if self in self.listeners:
            self.listeners.remove(self)
        if not self.listeners and self.periodic_callback:
            logger.debug('Stopping dashboard updates timer')
            self.periodic_callback.stop()
