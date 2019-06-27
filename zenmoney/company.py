#!/usr/bin/env python

from . import ZenObject, timestamp


class Company(ZenObject):
    '''
    Zenmoney bank or another company, see
    https://github.com/zenmoney/ZenPlugins/wiki/ZenMoney-API#company
    '''
    def __init__(self,
                 *,
                 id:         int,
                 changed:    int = timestamp(),
                 title:      str,
                 fullTitle:  str = None,  # could be empty
                 www:        str = None,  # could be empty
                 country:    str = None,  # could be empty
                 **kwargs,
                 ):
        self.id = id
        self.changed = changed
        self.title = title
        self.fullTitle = fullTitle
        self.www = www
        self.country = country
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return self.title
