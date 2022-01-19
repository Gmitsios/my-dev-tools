from datetime import datetime

import os
import sys
import inspect

# required to be able to add libraries from parent directory
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from db_engine import *


def _not_empty(val):
    if not val:
        raise ValidationError('value can not be empty')

class Trade(Document):
    asset1 = StringField(validation=_not_empty)
    asset0 = StringField(default="USDT")
    price_now = FloatField(min_value=0, default=.0)
    price_low_buy = FloatField(min_value=0, default=.0)
    price_high_buy = FloatField(min_value=0, default=.0)
    target_prices = FloatField(min_value=0, default=.0)
    stop_loss = FloatField(min_value=0, default=.0)
    signaled = DateTimeField(default=datetime.now())
    placed = DateTimeField() 
    cashed_out = DateTimeField()
    active = BooleanField(default=False)
    
    # def ltv_ratio(self):
    #     return self.ltv / 100
