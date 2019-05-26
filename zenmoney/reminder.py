#!/usr/bin/env python

from zenmoney import ZenObject, UUID, date, timestamp


class Reminder(ZenObject):
    '''
    ZenMoney reminder, see
    https://github.com/zenmoney/ZenPlugins/wiki/ZenMoney-API#reminder
    '''
    def __init__(self,
                 *,
                 id:                 UUID,  # UUID, string in original
                 changed:            int = timestamp(),
                 user:               UUID,  # User.id
                 incomeInstrument:   int,  # -> Instrument.id
                 incomeAccount:      UUID,  # -> Account.id
                 income:             float,  # >= 0
                 outcomeInstrument:  int,  # -> Instrument.id
                 outcomeAccount:     UUID,  # -> Account.id
                 outcome:            float,  # >= 0
                 # tag:              [String  -> Tag.id]?
                 # merchant:         UUID? -> Merchant.id
                 # payee:            String?
                 # originalPayee:    String?
                 # comment:          String?
                 interval:           str = None,  # See check in body
                 step:               int = 0,
                 points:             list = [],  # See check in body
                 startDate:          date,
                 endDate:            date = None,
                 notify:             bool,
                 **kwargs
                 ):
        self.id = id
        self.changed = changed
        self.user = user
        self.incomeInstrument = incomeInstrument
        self.incomeAccount = incomeAccount
        self.income = income
        self.outcomeInstrument = outcomeInstrument
        self.outcomeAccount = outcomeAccount
        self.outcome = outcome
        self.interval = interval
        self.step = step
        self.points = points
        self.startDate = startDate
        self.endDate = endDate
        self.notify = notify
        for k, v in kwargs.items():
            setattr(self, k, v)
