import time, traceback, sys
import schema
from log_utils import *

logger = logging.getLogger(__name__)
logger = init_logger(logger)


if __name__ == "__main__":
  try:
    logger.info("Hi from your Discord Bot!")
    logger.notify("Hi from a Notification!")
    logger.critical("This is critical!")
    logger.error("This is an error!")

    time.sleep(10000)
  
  except KeyboardInterrupt:
    print('Interrupted')
    try:
      sys.exit(0)
    except SystemExit:
      os._exit(0)