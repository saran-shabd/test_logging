import boto3
from botocore.exceptions import ClientError
from get_logger import Logger

# configure boto3 client
s3 = boto3.Session(profile_name='default').client('s3')
bucket_name = 'in.remaps.api.logs'

# configure logger instance
logger = Logger.get_logger(__name__)


def upload_latest_log(filename):
    """upload latest log file to Amazon S3"""

    try:
        s3.upload_file(filename, bucket_name, filename.split('/')[1])

        return True

    except ClientError as e:
        logger.warn('failed to upload latest log file to S3')

        return False


def delete_oldest_log(filename):
    """delete oldest log file from Amazon S3"""

    try:
        # s3.Bucket(bucket_name).Object(filename.split('/')[1]).delete()
        s3.delete_object(Bucket=bucket_name, Key=filename.split('/')[1])

    except Exception as e:
        logger.exception('failed to delete log file from S3')
