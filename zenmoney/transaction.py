#!/usr/bin/env python

# `date` used in Transaction init as well
from . import date as datetime_date
from . import ZenObject, UUID, timestamp


class Transaction(ZenObject):
    '''
    ZenMoney transaction, see
    https://github.com/zenmoney/ZenPlugins/wiki/ZenMoney-API#transaction
    '''
    def __init__(self,
                 *,
                 id:                     UUID,  # UUID, string in original
                 changed:                int = timestamp(),
                 created:                int = timestamp(),
                 user:                   UUID,  # User.id
                 deleted:                bool = False,
                 # hold:                 Bool?
                 incomeInstrument:       int,  # -> Instrument.id
                 incomeAccount:          UUID,  # -> Account.id
                 income:                 float,  # >= 0
                 outcomeInstrument:      int,  # -> Instrument.id
                 outcomeAccount:         UUID,  # -> Account.id
                 outcome:                float,  # >= 0
                 # tag:                  [String  -> Tag.id]?
                 # merchant:             UUID? -> Merchant.id
                 # payee:                String?
                 # originalPayee:        String?
                 # comment:              String?
                 date:                   datetime_date,  # 'yyyy-MM-dd'
                 # mcc:                  Int?
                 # reminderMarker:       String? -> ReminderMarker.id
                 # opIncome:             Double? >= 0
                 # opIncomeInstrument:   Int? -> Instrument.id
                 # opOutcome:            Double? >= 0
                 # opOutcomeInstrument:  Int? -> Instrument.id
                 # latitude:             Double? >= -90  && <= 90
                 # longitude:            Double? >= -180 && <= 180
                 **kwargs
                 ):
        self.id = id
        self.changed = changed
        self.created = created
        self.user = user
        self.deleted = deleted
        self.incomeInstrument = incomeInstrument
        self.incomeAccount = incomeAccount
        self.income = income
        self.outcomeInstrument = outcomeInstrument
        self.outcomeAccount = outcomeAccount
        self.outcome = outcome
        self.date = str(date)
        for k, v in kwargs.items():
            setattr(self, k, v)
