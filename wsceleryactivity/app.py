import logging

import celery
import tornado.gen
import tornado.web
from tornado import ioloop

from wsceleryactivity.urls import make_handlers

logger = logging.getLogger(__name__)


class WsCeleryActivity(tornado.web.Application):
    def __init__(self, capp, options, io_loop=None, **kwargs):
        self.io_loop = io_loop or ioloop.IOLoop.instance()
        self.capp = capp or celery.Celery()
        self.options = options
        kwargs.update(handlers=make_handlers(self.options))
        super().__init__(**kwargs)
        self.started = False

    @tornado.gen.coroutine
    def start(self):
        logger.info('Starting websocket listener on port %d'
                    % self.options.port)
        self.listen(self.options.port, address=self.options.address)
        self.started = True
        logger.debug('Starting event monitor')
        self.io_loop.start()

    def stop(self):
        if self.started:
            self.started = False
