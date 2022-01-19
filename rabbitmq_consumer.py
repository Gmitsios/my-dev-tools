from rabbitmq_producer import rabbitmq
from log_utils import *

logger = logging.getLogger(__name__)
logger = init_logger(logger)

consumer = rabbitmq


def callback(ch, method, properties, body):
    logger.info(f'{body} is received')
    
consumer.basic_consume(queue="test-queue", on_message_callback=callback, auto_ack=True)
consumer.start_consuming()