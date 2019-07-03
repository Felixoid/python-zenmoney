#!/usr/bin/env python

# `date` used in Transaction init as well
from . import date as datetime_date
from . import ZenObject, UUID, timestamp


class ReminderMarker(ZenObject):
    '''
    ZenMoney reminder marker, see
    https://github.com/zenmoney/ZenPlugins/wiki/ZenMoney-API#remindermarker
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
                 date:               datetime_date,  # yyyy-MM-dd
                 reminder:           UUID,  # -> Reminder.id
                 state:              str,  # planned, processed, deleted
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
        self.date = str(date)
        self.reminder = reminder
        self.state = state
        self.notify = notify
        for k, v in kwargs.items():
            setattr(self, k, v)
