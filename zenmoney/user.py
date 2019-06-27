#!/usr/bin/env python

from . import ZenObject, timestamp


class User(ZenObject):
    '''
    Zenmoney User, see
    https://github.com/zenmoney/ZenPlugins/wiki/ZenMoney-API#user
    '''
    def __init__(self,
                 *,
                 id:        int,
                 changed:   int = timestamp(),
                 login:     str = None,  # could be empty
                 currency:  int,  # Instrument.id
                 parent:    int = None,  # User.id, could be empty
                 **kwargs,
                 ):
        self.id = id
        self.changed = changed
        self.login = login
        self.currency = currency
        self.parent = parent
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return self.login
