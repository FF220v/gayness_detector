from aiohttp import web
from asyncio import gather
from src.redis import get_data_many_keys, get_data_for_all_keys, put_data, get_keys, delete_key
from src.logger import Logger
from src.artificial_intelligence import get_gayness_coefficient

log = Logger.get_logger_by_name(__name__)


async def cleanup_handler(req):
    status, data = await get_keys()
    if status == 200:
        responses = await gather(*[delete_key(key) for key in data])
        if all(status == 200 for status, _ in responses):
            return web.json_response({'status': 'ok'})
    return web.json_response({'status': 'error', 'error': 'Cannot clean up'}, status=500)


async def post_handler(req):
    key = req.match_info['object_id']
    data = {'gayness': get_gayness_coefficient(key)}
    status, response = await put_data(key, data)
    if status == 200:
        return web.json_response({'status': 'ok'})
    else:
        return web.json_response({'status': 'error', 'error': 'Cannot put data'}, status=500)


async def delete_handler(req):
    key = req.match_info['object_id']
    status, response = await delete_key(key)
    if status == 200:
        return web.json_response({'status': 'ok'})
    else:
        return web.json_response({'status': 'error', 'error': 'Cannot delete key'}, status=500)


async def get_handler(req):
    key = req.match_info.get('object_id')
    if key:
        status, response = await get_data_many_keys([key])
        if status == 200:
            return web.json_response({'status': 'ok', 'data': response})
        else:
            return web.json_response({'status': 'error', 'error': 'Cannot get data'}, status=500)
    else:
        status, response = await get_data_for_all_keys()
        if status == 200:
            return web.json_response({'status': 'ok', 'data': response})
        else:
            return web.json_response({'status': 'error', 'error': 'Cannot get data'}, status=500)


post_handlers = [
    ('/cleanup', cleanup_handler),
    ('/{object_id}', post_handler),
]

get_handlers = [
    ('/', get_handler),
    ('/{object_id}', get_handler)
]

delete_handlers = [
    ('/{object_id}', delete_handler)
]

app = web.Application()

for path, handler in get_handlers:
    app.add_routes([web.get(path, handler)])

for path, handler in post_handlers:
    app.add_routes([web.post(path, handler)])

for path, handler in delete_handlers:
    app.add_routes([web.delete(path, handler)])


def main():
    web.run_app(app, host='0.0.0.0', port=8080)


if __name__ == "__main__":
    main()
