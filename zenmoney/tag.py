#!/usr/bin/env python

from . import ZenObject, UUID, timestamp


class Tag(ZenObject):
    '''
    Zenmoney transaction tag or category, see
    https://github.com/zenmoney/ZenPlugins/wiki/ZenMoney-API#tag
    '''
    def __init__(self,
                 *,
                 id:             UUID,  # UUID, string in original
                 changed:        int = timestamp(),
                 user:           UUID,  # User.id
                 title:          str,
                 # parent:       String? -> Tag.id
                 # icon:         String?
                 # picture:      String?
                 # * color = (a << 24) + (r << 16) + (g << 8) + (b << 0)
                 # color:        Int?
                 showIncome:     bool,
                 showOutcome:    bool,
                 budgetIncome:   bool,
                 budgetOutcome:  bool,
                 required:       bool = False,  # true if null o_O
                 **kwargs,
                 ):
        self.id = id
        self.changed = changed
        self.user = user
        self.title = title
        self.showIncome = showIncome
        self.showOutcome = showOutcome
        self.budgetIncome = budgetIncome
        self.budgetOutcome = budgetOutcome
        self.required = required
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return self.title
