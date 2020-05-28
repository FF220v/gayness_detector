from random import randint
from src.logger import Logger

log = Logger.get_logger_by_name(__name__)


def get_gayness_coefficient(name: str) -> int:
    if 'Egor' in name:
        result = randint(90, 100)
    elif 'Sa' in name:
        result = randint(0, 10)
    else:
        result = randint(0, 100)
    log.info(f'Gay coefficient for {name} is {result}')
    return result

