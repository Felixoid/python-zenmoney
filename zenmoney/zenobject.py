#!/usr/bin/env python


def to_dict(obj, classkey=None):
    if isinstance(obj, dict):
        data = {}
        for (k, v) in obj.items():
            data[k] = ZenObject._to_dict(v, classkey)

        return data
    elif hasattr(obj, '__iter__') and not isinstance(obj, str):
        return [ZenObject._to_dict(v, classkey) for v in obj]
    elif hasattr(obj, '__dict__'):
        data = dict([
            (key, ZenObject._to_dict(getattr(obj, key), classkey))
            for key in obj.__dir__()
            if not key.startswith('_')
            and not callable(getattr(obj, key))
        ])
        if classkey is not None and hasattr(obj, '__class__'):
            data[classkey] = obj.__class__.__name__
        return data
    else:
        return obj


class ZenObject(object):
    '''
    The common methods of ZenMoney objects
    '''

    def __int__(self):
        return int(self.id)

    def __eq__(self, obj):
        return int(self) == int(obj)

    def _type(self):
        return type(self).__name__

    def _to_dict(self, classkey=None):
        return to_dict(self, classkey)
