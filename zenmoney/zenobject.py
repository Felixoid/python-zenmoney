#!/usr/bin/env python


def to_dict(obj, classkey=None):
    if isinstance(obj, dict):
        data = {}
        for (k, v) in obj.items():
            data[k] = to_dict(v, classkey)

        return data
    elif hasattr(obj, '__iter__') and not isinstance(obj, str):
        return [to_dict(v, classkey) for v in obj]
    elif hasattr(obj, '__dict__'):
        data = dict([
            (key, to_dict(getattr(obj, key), classkey))
            # __dir__ is used here to get dynamic properties
            # like Diff.currentClientTimestamp as well
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

    def to_dict(self, classkey=None):
        return to_dict(self, classkey)


class ZenObjectsList(list):
    def by_account(self, value):
        # Is dedicated because looking by two attributes
        for o in self:
            if o.incomeAccount == value or o.outcomeAccount == value:
                yield o

    def by_id(self, value):
        return self._by_attr_uniq('id', value)

    def by_incomeAccount(self, value):
        return self._by_attr('incomeAccount', value)

    def by_outcomeAccount(self, value):
        return self._by_attr('outcomeAccount', value)

    def by_shortTitle(self, value):
        return self._by_attr_uniq('shortTitle', value)

    def by_symbol(self, value):
        return self._by_attr_uniq('symbol', value)

    def by_tag(self, value):
        return self._by_attr('tag', value)

    def by_title(self, value):
        return self._by_attr_uniq('title', value)

    def by_user(self, value):
        return self._by_attr('user', value)

    def _by_attr_uniq(self, attr, value):
        for o in self:
            attr_value = getattr(o, attr)
            if hasattr(attr_value, '__iter__'):
                if value in attr_value or value == attr_value:
                    return o
            else:
                if value == attr_value:
                    return o

    def _by_attr(self, attr, value):
        for o in self:
            attr_value = getattr(o, attr)
            if hasattr(attr_value, '__iter__'):
                if value in attr_value or value == attr_value:
                    yield o
            else:
                if value == attr_value:
                    yield o

    def to_dict(self, classkey=None):
        return to_dict(self, classkey)
