#!/usr/bin/env python

# `date` used in Transaction init as well
from . import date as datetime_date
from . import ZenObject, UUID, timestamp


class Budget(ZenObject):
    '''
    Zenmoney bank or another company, see
    https://github.com/zenmoney/ZenPlugins/wiki/ZenMoney-API#company
    '''
    def __init__(self,
                 *,
                 changed:      int = timestamp(),
                 user:         int,  # User.id
                 tag:          UUID,  # Tag.id
                 date:         datetime_date,  # yyyy-MM-dd
                 income:       float,
                 incomeLock:   bool,
                 outcome:      float,
                 outcomeLock:  bool,
                 **kwargs,
                 ):
        self.changed = changed
        self.user = user
        self.tag = tag
        self.date = str(date)
        self.income = income
        self.incomeLock = incomeLock
        self.outcome = outcome
        self.outcomeLock = outcomeLock
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return self.login
