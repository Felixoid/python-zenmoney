#!/usr/bin/env python

from . import ZenObject, UUID, timestamp


class Account(ZenObject):
    '''
    ZenMoney account, see
    https://github.com/zenmoney/ZenPlugins/wiki/ZenMoney-API#account
    '''
    def __init__(self,
                 *,
                 id:                       UUID,  # UUID, string in original
                 changed:                  int = timestamp(),
                 user:                     UUID,  # User.id
                 # role:                   Int? -> User.id?
                 instrument:               int = None,  # -> Instrument.id
                 company:                  int = None,  # -> Company.id
                 type:                     str,  # See check in body
                 # balance:                Double?
                 # startBalance:           Double?
                 # creditLimit:            Double? >= 0
                 inBalance:                bool,
                 # savings:                Bool?
                 enableCorrection:         bool,
                 enableSMS:                bool,
                 archive:                  bool,
                 # capitalization:         Bool
                 # percent:                Double >= 0 && < 100
                 # startDate:              'yyyy-MM-dd'
                 # endDateOffset:          Int
                 # endDateOffsetInterval:  ('day' | 'week' | 'month' | 'year')
                 # payoffStep:             Int?
                 # payoffInterval:         ('month' | 'year')?
                 **kwargs,
                 ):
        self.id = id
        self.changed = changed
        self.user = user
        self.instrument = instrument
        self.company = company
        valid_type = ['cash', 'ccard', 'checking', 'loan', 'deposit',
                      'emoney', 'debt']
        if type not in valid_type:
            raise(ValueError('"type" should be in {}'.format(valid_type)))
        self.type = type
        self.inBalance = inBalance
        self.enableCorrection = enableCorrection
        self.enableSMS = enableSMS
        self.archive = archive
        for k, v in kwargs.items():
            setattr(self, k, v)
