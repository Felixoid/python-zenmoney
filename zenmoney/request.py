#!/usr/bin/env python

import requests
from zenmoney import API_URL, timestamp


class Request(object):

    uri_diff = API_URL + '/v8/diff/'
    uri_suggest = API_URL + '/v8/suggest/'

    def __init__(self, token: str):
        self.s = requests.Session()
        self.s.headers['Authorization'] = 'Bearer {}'.format(token)
        self.s.headers['Content-Type'] = 'application/json'

    def diff(self, data: dict, server_timestamp: int = None) -> dict:
        if 'serverTimestamp' not in data:
            data['serverTimestamp'] = server_timestamp
        if 'currentClientTimestamp' not in data:
            data['currentClientTimestamp'] = timestamp()

        response = self.s.post(self.uri_diff, json=data)
        return response.json()

    def suggest(self, transactions: list) -> list:
        response = self.s.post(self.uri_suggest, json=transactions)
        return response.json()
