#!/usr/bin/env python

from zenmoney import timestamp, ZenObject


class Instrument(ZenObject):
    '''
    Zenmoney currency, read-only, see
    https://github.com/zenmoney/ZenPlugins/wiki/ZenMoney-API#instrument
    '''
    def __init__(self,
                 *,
                 id:          int,
                 changed:     int = timestamp(),
                 title:       str,
                 shortTitle:  str,  # 3 letters code
                 symbol:      str,
                 rate:        float,  # relative to RUB
                 **kwargs,
                 ):
        self.id = id
        self.changed = changed
        self.title = title
        self.shortTitle = shortTitle
        self.symbol = symbol
        self.rate = rate
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return self.title
