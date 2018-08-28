import asyncio
import json
import vmprof
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


if __name__ == '__main__':
    import socket as S
    import argparse
    import pathlib

    ap = argparse.ArgumentParser()
    ap.add_argument('--profile', default=None, type=pathlib.Path,
                    help="Enable vmprof and write profile into specified file")
    opts = ap.parse_args()

    def run_on_shared_socket():
        with S.socket(S.AF_INET, S.SOCK_STREAM | S.SOCK_NONBLOCK) as sock:
            sock.setsockopt(S.SOL_SOCKET, S.SO_REUSEADDR, 1)
            sock.setsockopt(S.SOL_SOCKET, S.SO_REUSEPORT, 1)
            sock.bind(('127.0.0.1', 5000))
            app = init(None)
            web.run_app(app, sock=sock)

    if opts.profile is not None:
        with opts.profile.open('w+b') as f:
            vmprof.enable(f.fileno())
            try:
                run_on_shared_socket()
            finally:
                vmprof.disable()
    else:
        run_on_shared_socket()
