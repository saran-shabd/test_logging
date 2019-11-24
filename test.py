import another_test
from get_logger import Logger
import time

logger = Logger.get_logger(__name__)


def main():
    
    logger.info('Application Started')

    another_test.do_something()

    logger.debug('this is a debug message for the logger to test')

    logger.error('memory leak')

    logger.info('Application Died')


if __name__ == "__main__":
    main()
