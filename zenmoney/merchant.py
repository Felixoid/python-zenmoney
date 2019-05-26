#!/usr/bin/env python

from zenmoney import ZenObject, UUID, timestamp


class Merchant(ZenObject):
    '''
    Zenmoney Merchant, see
    https://github.com/zenmoney/ZenPlugins/wiki/ZenMoney-API#merchant
    '''
    def __init__(self,
                 *,
                 id:       UUID,  # UUID, string in original
                 changed:  int = timestamp(),
                 user:     UUID,  # User.id
                 title:    str,
                 **kwargs,
                 ):
        self.id = id
        self.changed = changed
        self.user = user
        self.title = title
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return self.title
