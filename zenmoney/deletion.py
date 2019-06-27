#!/usr/bin/env python

from . import (
    API_OBJECTS,
    timestamp,
    ZenMoneyException,
    ZenObject,
)


class Deletion(ZenObject):
    '''
    Object which is defining which objects should be deleted on a client or
    the server site.
    See https://github.com/zenmoney/ZenPlugins/wiki/ZenMoney-API#diff-object
    '''

    def __init__(self,
                 *,
                 id:      str,
                 object:  str,
                 stamp:   int = timestamp(),
                 user:    int,
                 **kwargs,
                 ):
        if object not in [obj.lower() for obj in API_OBJECTS]:
            raise ZenMoneyException('The object {} is unknown'.format(object))
        self.id = id
        self.object = object
        self.stamp = stamp
        self.user = user
