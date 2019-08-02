#!/usr/bin/env python

from datetime import datetime  # noqa:F401


VERSION = (0, 9)
API_URL = 'https://api.zenmoney.ru'
API_OBJECTS = ['Account', 'Budget', 'Company', 'Instrument', 'Merchant',
               'Reminder', 'ReminderMarker', 'Tag', 'Transaction', 'User']


def timestamp(d: datetime = None):
    if d:
        return int(datetime.timestamp(d))
    else:
        return int(datetime.timestamp(datetime.now()))


from .exception import ZenMoneyException  # noqa:F401
from .zenobject import ZenObject, ZenObjectsList  # noqa:F401

from .account import Account  # noqa:F401
from .budget import Budget  # noqa:F401
from .company import Company  # noqa:F401
from .instrument import Instrument  # noqa:F401
from .merchant import Merchant  # noqa:F401
from .reminder import Reminder  # noqa:F401
from .reminder_marker import ReminderMarker  # noqa:F401
from .tag import Tag  # noqa:F401
from .transaction import Transaction  # noqa:F401
from .user import User  # noqa:F401

from .deletion import Deletion  # noqa:F401
from .diff import Diff  # noqa:F401
from .oauth2 import OAuth2  # noqa:F401
from .request import Request  # noqa:F401
