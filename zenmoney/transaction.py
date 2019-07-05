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
                 tag:                    list = None,  # [String  -> Tag.id]?
                 merchant:               UUID = None,  # -> Merchant.id
                 payee:                  str = None,
                 # originalPayee:        String?
                 # comment:              String?
                 date:                   datetime_date,  # 'yyyy-MM-dd'
                 # mcc:                  Int?
                 reminderMarker:         str = None,  # -> ReminderMarker.id
                 opIncome:               float = None,  # >= 0
                 opIncomeInstrument:     int = None,  # -> Instrument.id
                 opOutcome:              float = None,  # >= 0
                 opOutcomeInstrument:    int = None,  # -> Instrument.id
                 latitude:               float = None,  # >= -90  && <= 90
                 longitude:              float = None,  # >= -180 && <= 180
                 incomeBankID:           str = None,  # ???
                 outcomeBankID:          str = None,  # ???
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
        self.tag = tag
        self.merchant = merchant
        self.payee = payee
        self.reminderMarker = reminderMarker
        self.opIncome = opIncome
        self.opIncomeInstrument = opIncomeInstrument
        self.opOutcome = opOutcome
        self.opOutcomeInstrument = opOutcomeInstrument
        self.incomeBankID = incomeBankID
        self.outcomeBankID = outcomeBankID
        self.longitude = longitude
        self.latitude = latitude
        self.date = str(date)
        for k, v in kwargs.items():
            setattr(self, k, v)
