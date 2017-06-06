import logging

import tornado.ioloop
import tornado.web
import tornado.websocket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8646

logging.basicConfig(level=logging.WARNING)


class EchoWebSocket(tornado.websocket.WebSocketHandler):

    def on_message(self, message):
        self.write_message(message, binary=isinstance(message, bytes))


app = tornado.web.Application(
    [
        (r'/', EchoWebSocket)
    ],
    websocket_max_message_size=2 ** 25)
app.listen(SERVER_PORT, SERVER_HOST)
tornado.ioloop.IOLoop.current().start()
