from get_logger import Logger

logger = Logger.get_logger(__name__)


def do_something():
    """Function to test modular logging"""

    logger.warn('I did something')
