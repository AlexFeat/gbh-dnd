import logging
from functools import lru_cache
from hashlib import sha256

from rich.console import Console
from rich.logging import RichHandler

from app.settings import get_settings


console = Console(color_system="256", width=200, style="blue")
settings = get_settings()


@lru_cache()
def get_logger(module_name):
    logger = logging.getLogger(module_name)
    handler = RichHandler(rich_tracebacks=True, console=console, tracebacks_show_locals=True)
    handler.setFormatter(logging.Formatter("[ %(threadName)s:%(funcName)s:%(lineno)d ] - %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger


def password_hash(pwd: str):
    return sha256(f'{pwd}{settings.PWD_SALT}'.encode()).hexdigest()
