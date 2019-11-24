import another_test
from s3 import upload_latest_log, delete_oldest_log
from datetime import datetime, timedelta
import os
import logging
import logging.config


def setup_logging():
    """setup logging configurations for the application"""

    # create logs directory
    try:
        os.mkdir('logs')
    except OSError:  # directory already exists
        pass
    
    # configurer logger
    logging.config.fileConfig('logging.conf')


def main():

    setup_logging()

    logger = logging.getLogger(__name__)

    another_test.do_something()

    logger.debug('this is a debug message for the logger to test')

    logger.error('memory leak')

    logger.info('Application Died')

    logger.warn('i also did something')

    today = datetime.now()
    yesterday = today - timedelta(days=1)
    today = today.strftime('%Y-%m-%d')
    yesterday = yesterday.strftime('%Y-%m-%d')

    # upload yesterday's log file to S3
    if upload_latest_log(filename='logs/app.log.' + today):
        
        # delete yesterday's log file from disk memory
        os.remove('logs/app.log.' + today)

    # delete last month's log file from S3
    delete_oldest_log(filename='logs/app.log.' + today)


if __name__ == "__main__":
    main()
