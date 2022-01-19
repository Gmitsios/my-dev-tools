import os
from datetime import datetime
from dotenv import load_dotenv
from mongoengine import *

load_dotenv()

connect(
  db=os.getenv('DB_NAME'),
  host=os.getenv('DB_HOST'),
  port=int(os.getenv('DB_PORT'))
)


def _not_empty(val):
  if not val:
    raise ValidationError('value can not be empty')

class Notification(Document):
  msg = StringField(validation=_not_empty)
  source = StringField()
  file = StringField()
  level = StringField()
  channel = StringField()
  type = StringField()
  created = DateTimeField(default=datetime.now())
  sent = BooleanField(default=False)
