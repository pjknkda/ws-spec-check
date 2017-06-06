import asyncio
import logging

import aiohttp
from aiohttp import web

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8644

logging.basicConfig(level=logging.WARNING)


async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            await ws.send_str(msg.data)
        elif msg.type == aiohttp.WSMsgType.BINARY:
            await ws.send_bytes(msg.data)
        elif msg.type == aiohttp.WSMsgType.ERROR:
            break

    return ws

app = web.Application()
app.router.add_get('/', websocket_handler)
web.run_app(app,
            host=SERVER_HOST,
            port=SERVER_PORT)
