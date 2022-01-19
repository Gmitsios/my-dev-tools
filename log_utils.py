import logging, os, traceback
from db_engine import *

# init logger like this
# logger = logging.getLogger(__name__)
# logger = init_logger(logger)

# set root logging level to minimum so it will output any level we want on our handlers
logging.root.setLevel(logging.NOTSET)

# add logging level for notifications
logging.NOTIFICATION_LEVELV_NUM = logging.CRITICAL - 5
logging.addLevelName(logging.NOTIFICATION_LEVELV_NUM, "NOTIFICATION")
def notify(self, message, *args, **kws):
  if self.isEnabledFor(logging.NOTIFICATION_LEVELV_NUM):
    # Yes, logger takes its '*args' as 'args'.
    self._log(logging.NOTIFICATION_LEVELV_NUM, message, args, **kws) 
logging.getLoggerClass().notify = notify


def init_logger(logger):

  # Create handlers
  stream_handler = logging.StreamHandler()
  file_handler = logging.FileHandler('logs/{}-app.log'.format(os.getenv('APPNAME')))
  db_handler = MongoNotificationHandler()

  # Configure level and formatter and add it to handlers
  stream_handler.setLevel(logging.DEBUG) # warning and above is logged to the stream
  file_handler.setLevel(logging.INFO) # error and above is logged to a file
  db_handler.setLevel(logging.NOTIFICATION_LEVELV_NUM)

  stream_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
  file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
  stream_handler.setFormatter(stream_format)
  file_handler.setFormatter(file_format)
  db_handler.setFormatter(stream_format)

  # Add handlers to the logger
  logger.addHandler(stream_handler)
  logger.addHandler(file_handler)
  logger.addHandler(db_handler)

  return logger


class MongoNotificationHandler(logging.Handler):

  def emit(self, record):
    trace = None
    exc = record.__dict__['exc_info']
    if exc:
        trace = traceback.format_exc() ##CHANGE HERE, removed exc parameter
    Notification(
      msg=record.__dict__['msg'],
      source=record.__dict__['name'],
      level=record.__dict__['levelname']
    ).save()
