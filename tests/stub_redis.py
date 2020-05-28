from aiohttp import web


STUB_REDIS_PORT = 8081
STUB_REDIS_HOST = "127.0.0.1"


app = web.Application()


def run_redis_stub():
    web.run_app(app, host=STUB_REDIS_HOST, port=STUB_REDIS_PORT)