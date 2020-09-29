import boto3
import botocore

from ..logger import get_logger
from ..client import AWSClientWrapper


class CloudWatch:
    """Wrapper around boto3 to fetch CloudWatch logs
    """
    def __init__(self):
        self.logger = get_logger(self.__class__.__name__)
        self._client_wrapper = AWSClientWrapper(service='cloudwatch')
        self._client = self._client_wrapper.client
