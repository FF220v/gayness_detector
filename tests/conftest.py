import pytest
from multiprocessing import Process
from src.worker import main as run_server
from tests.stub_redis import STUB_REDIS_PORT, STUB_REDIS_HOST, run_redis_stub


@pytest.fixture()
def run_test_server():
    p = Process(target=run_server)
    p.start()
    yield p
    p.kill()


@pytest.fixture()
def run_redis_stub():
    p = Process(target=run_redis_stub)
    p.start()
    yield p
    p.kill()
