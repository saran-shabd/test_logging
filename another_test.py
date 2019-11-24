
import logging
from get_logger import get_logger

# create new logger
logger = get_logger(__name__)


def do_something():
    """Function to test modular logging"""

    logger.warn('I did something')
