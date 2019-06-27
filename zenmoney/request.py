#!/usr/bin/env python

import requests
from . import API_URL, Diff, Transaction


class Request(object):

    uri_diff = API_URL + '/v8/diff/'
    uri_suggest = API_URL + '/v8/suggest/'

    def __init__(self, token: str):
        self.s = requests.Session()
        self.s.headers['Authorization'] = 'Bearer {}'.format(token)
        self.s.headers['Content-Type'] = 'application/json'

    def diff(self, diff: Diff, debug=False) -> Diff:
        '''
        Accept the Diff object and returns Diff object
        '''
        response = self.s.post(self.uri_diff, json=Diff._to_dict(diff))
        if debug:
            self._plain_diff = response.json()

        return Diff(**response.json())

    def suggest(self, transaction) -> Transaction:
        '''
        Accept one or list of Transactions,
        returns the same data with suggestions
        '''
        response = self.s.post(self.uri_suggest,
                               json={'transaction': transaction})
        return response.json()
