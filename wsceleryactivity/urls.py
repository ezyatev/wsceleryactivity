from tornado.web import url

from wsceleryactivity.websocket import WebSocketHandler


def make_handlers(options):
    return [
        url(r'/tasks', WebSocketHandler, {
            'allow_origin': options.allow_origin,
        }),
    ]