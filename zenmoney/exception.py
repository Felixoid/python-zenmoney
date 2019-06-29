#!/usr/bin/env python


class ZenMoneyException(Exception):
    def __init__(self, message, **kwargs):
        self.__dict__.update(kwargs)
        Exception.__init__(self, message)
