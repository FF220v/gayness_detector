from src.http_async import get, put
from src.urls import REDIS_HTTP_URL
import json
from src.logger import Logger

log = Logger.get_logger_by_name(__name__)


def get_cmd_url(cmd, *args):
    url = f'{REDIS_HTTP_URL}/{cmd}/{"/".join(args)}'
    return url


async def get_keys():
    status, data = await get(get_cmd_url('KEYS', '*'))
    if status == 200:
        data = data['KEYS']
    log.info(f"Got keys. Status: {status}, Data: {data}")
    return status, data


async def put_data(key: str, data: dict):
    log.info(f"Put data. Key: {key}, Data: {data}")
    status, data = await put(get_cmd_url('SET', key), data)
    log.info(f"Put data. Status: {status}, Data: {data}")
    return status, data


async def get_data_many_keys(keys_list: list) -> (int, dict):
    log.info(f"Get data. Keys: {keys_list}")
    status, data = await get(get_cmd_url('MGET', *keys_list))
    if status == 200:
        data = data['MGET']
        data = {n: (json.loads(d) if d is not None else d)
                for n, d in zip(keys_list, data)}
    log.info(f"Got data. Status: {status}, Data: {data}")
    return status, data


async def get_data(key: str) -> (int, dict):
    return await get_data_many_keys([key])


async def get_data_for_all_keys():
    status, keys = await get_keys()
    return await get_data_many_keys(keys)


async def delete_key(key: str) -> (int, dict):
    log.info(f"Delete data. Key: {key}")
    status, data = await get(get_cmd_url('DEL', key))
    log.info(f"Deleted data. Status: {status}, Response: {data}")
    return status, data
