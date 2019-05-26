#!/usr/bin/env python

from datetime import date, datetime  # noqa:F401
from uuid import UUID  # noqa:F401
from zenmoney import (  # noqa:F401
                      Account,
                      Instrument,
                      Merchant,
                      OAuth2,
                      Request,
                      Transaction,
                      User,
)


VERSION = (0, 9)
API_URL = 'https://api.zenmoney.ru'


def timestamp(d: datetime = datetime.now()):
    return int(datetime.timestamp(d))


def ZenmoneyException(Exception):
    pass
