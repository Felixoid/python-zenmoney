#!/usr/bin/env python


class ZenObject(object):
    '''
    The common methods of ZenMoney objects
    '''

    def __int__(self):
        return int(self.id)

    def __eq__(self, obj):
        return int(self) == int(obj)
