import pika, os
from dotenv import load_dotenv
from log_utils import *

logger = logging.getLogger(__name__)
logger = init_logger(logger)

load_dotenv()

connection = pika.BlockingConnection(
  pika.ConnectionParameters(
    os.getenv('PIKA_HOST'),
    int(os.getenv('PIKA_PORT')),
    '/',
    pika.PlainCredentials(os.getenv('PIKA_USER'), os.getenv('PIKA_PASS'))
  )
)

rabbitmq = connection.channel()
logger.info("Rabbit-MQ connection established")
