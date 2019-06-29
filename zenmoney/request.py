#!/usr/bin/env python

import requests
from . import API_URL, Diff, Transaction, ZenMoneyException


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
        response = self.__post(self.uri_diff, Diff._to_dict(diff))
        if debug:
            self._plain_diff = response.json()

        return Diff(**response.json())

    def suggest(self, transaction: object) -> Transaction:
        '''
        Accept one or list of Transactions,
        returns the same data with suggestions
        '''
        response = self.__post(self.uri_suggest,
                               {'transaction': transaction})
        return response.json()

    def __post(self, uri: str, data: object, **kwargs):
        '''
        Wrapper for request.post, which raises exception on non ok results
        '''
        response = self.s.post(uri, json=data, **kwargs)
        if not response.ok:
            raise ZenMoneyException('Diff request wasn\'t successful',
                                    uri=uri, response=response)
