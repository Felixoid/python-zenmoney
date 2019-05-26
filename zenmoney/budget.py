#!/usr/bin/env python

# `date` used in Transaction init as well
from zenmoney import date as datetime_date
from zenmoney import ZenObject, UUID, timestamp


class Budget(ZenObject):
    '''
    Zenmoney bank or another company, see
    https://github.com/zenmoney/ZenPlugins/wiki/ZenMoney-API#company
    '''
    def __init__(self,
                 *,
                 id:              UUID,
                 changed:         int = timestamp(),
                 user:            int,  # User.id
                 tag:             UUID,  # Tag.id
                 date:            datetime_date,  # yyyy-MM-dd
                 income:          float,  # >= 0
                 incomeAccount:   str,  # -> Account.id
                 outcome:         float,  # >= 0
                 outcomeAccount:  str,  # -> Account.id
                 **kwargs,
                 ):
        self.id = id
        self.changed = changed
        self.user = user
        self.tag = tag
        self.date = date
        self.income = income
        self.incomeAccount = incomeAccount
        self.outcome = outcome
        self.outcomeAccount = outcomeAccount
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return self.login
