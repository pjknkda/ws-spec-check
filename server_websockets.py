import asyncio
import logging

import websockets

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8643

logging.basicConfig(level=logging.WARNING)


@asyncio.coroutine
def echo(ws, path):
    while True:
        try:
            msg = yield from ws.recv()
            yield from ws.send(msg)
        except websockets.ConnectionClosed:
            break


start_server = websockets.serve(echo,
                                SERVER_HOST,
                                SERVER_PORT,
                                max_size=2 ** 25,
                                max_queue=1)

try:
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt:
    pass
