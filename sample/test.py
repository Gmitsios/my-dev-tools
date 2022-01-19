import time, traceback
import schema
from log_utils import *
from rabbitmq_producer import rabbitmq

logger = logging.getLogger(__name__)
logger = init_logger(logger)


def test():
  print("Hi from your Discord Bot!")

  schema.Trade(asset1="TEST").save()
  logger.debug("This is debug msg")
  logger.info("This in info msg")
  rabbitmq.basic_publish(exchange='test-exchange', routing_key='test-routing-key', body='Test!')

  items = schema.Trade.objects()
  print("Found {} trades".format(len(items)))

test()