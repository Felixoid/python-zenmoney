#!/usr/bin/env python

from . import (  # noqa:F401
    API_OBJECTS,
    timestamp,

    Account,
    Budget,
    Company,
    Instrument,
    Merchant,
    Reminder,
    ReminderMarker,
    Tag,
    Transaction,
    User,

    Deletion,
    ZenObject,
)


class Diff(ZenObject):
    '''
    The main class to interract with ZenMoney API
    See https://github.com/zenmoney/ZenPlugins/wiki/ZenMoney-API#diff-object
    '''

    def __init__(self,
                 *,
                 serverTimestamp:         int,  # should be saved from request
                 # Dynamic in property
                 # currentClientTimestamp:  int = timestamp(),
                 # Everything further could be empty
                 # Which class should be fetched for the whole history
                 forceFetch:              list = [],
                 # Lists of received objects or objects to send
                 account:                 list = [],
                 budget:                  list = [],
                 company:                 list = [],
                 instrument:              list = [],
                 merchant:                list = [],
                 reminder:                list = [],
                 reminderMarker:          list = [],
                 tag:                     list = [],
                 transaction:             list = [],
                 user:                    list = [],
                 # Which objects were deleted on the server or a client site
                 deletion:                list = [],
                 **kwargs,
                 ):
        for class_name in API_OBJECTS + ['Deletion']:
            attr_name = class_name[0].lower() + class_name[1:]
            attr_value = locals()[attr_name]
            if attr_value:
                self.__fill_attribute(class_name, attr_value)

        if forceFetch:
            self.forceFetch = forceFetch

        self.serverTimestamp = serverTimestamp

    @property
    def currentClientTimestamp(self):
        return timestamp()

    def __fill_attribute(self, class_name: str, data: list):
        attr_name = class_name[0].lower() + class_name[1:]
        cls = globals()[class_name]
        attr_value = []
        for obj in data:
            try:
                attr_value.append(cls(**obj))
            except Exception as e:
                print(obj, class_name)
                print(e)
        setattr(self, attr_name, attr_value)
