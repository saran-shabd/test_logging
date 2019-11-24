import logging


def do_something():
    """Function to test modular logging"""

    logger = logging.getLogger(__name__)

    logger.warn('I did something')

    logger.warn('why the fuck am i not comming in logs???')

    logger.info('okay, so this should come in the logs')
