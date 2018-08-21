import asyncio
import json
from aiohttp import web


async def handle(request):
    return web.Response(text="Hello World!")


async def huge_json(request):
    return web.Response(text=_dump())


async def huge_json_thread(request):
    data = await asyncio.get_event_loop().run_in_executor(None, _dump)
    return web.Response(text=data)


async def lock_fast(request):
    async with lock:
        return web.Response(text='ok')


async def lock_slow(request):
    async with lock:
        await asyncio.sleep(.2)
        return web.Response(text='ok')

lock = asyncio.Lock()


def _dump():
    return json.dumps(list(range(10**5)))


def init(argv):
    app = web.Application()
    app.router.add_get('/', handle)
    app.router.add_get('/huge-json', huge_json)
    app.router.add_get('/huge-json-thread', huge_json_thread)
    app.router.add_get('/lock/fast', lock_fast)
    app.router.add_get('/lock/slow', lock_slow)
    return app
