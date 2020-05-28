import aiohttp
import json
from json.decoder import JSONDecodeError
from src.logger import Logger

log = Logger.get_logger_by_name(__name__)


async def make_request(url, method, data):
    async with aiohttp.ClientSession() as session:
        async with session.request(method=method, url=url, json=data) as resp:
            resp_data = await resp.text()
            try:
                resp_data = json.loads(resp_data)
            except JSONDecodeError:
                log.info('Invalid json data. Wrapping text.')
                resp_data = dict(text=resp_data)
            return resp.status, resp_data


async def get(url):
    return await make_request(url, method='GET', data=None)


async def put(url, data):
    return await make_request(url, method='PUT', data=data)
