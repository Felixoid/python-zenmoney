#!/usr/bin/env python

'''
Get oauth token for further requests to the API

You need to get a consumer_key and consumer_secret from
http://api.zenmoney.ru/consumer.html
and use your username and password then.
'''
import requests


class OAuth2(object):

    url_auth = 'https://api.zenmoney.ru/oauth2/authorize/'
    url_token = 'https://api.zenmoney.ru/oauth2/token/'
    url_redirect = 'notscheme://localhost/'

    def __init__(self, consumer_key: str, consumer_secret: str,
                 username: str, password: str):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.username = username
        self.password = password
        self.s = requests.Session()

    def __get_token(self):
        if hasattr(self, '_token'):
            return self._token
        else:
            self.__set_token()
            return self._token

    def __set_token(self):
        'request cookie'
        'request code'
        'request token'
        if hasattr(self, '_token'):
            return

        code = self._get_code()
        response = self.s.post(
            self.url_token,
            data={
                'grant_type': 'authorization_code',
                'client_id': self.consumer_key,
                'client_secret': self.consumer_secret,
                'code': code,
                'redirect_uri': self.url_redirect,
            }
        )

        self._token = response.json()['access_token']
        self._token_response = response.json()

    def _get_code(self):
        '''
        Get auth cookie, authorize user and then get the code for token
        '''
        self.s.get(
            self.url_auth,
            params={
                'response_type': 'code',
                'client_id': self.consumer_key,
                'redirect_uri': self.url_redirect,
            }
        )
        response = self.s.post(
            self.url_auth,
            data={
                'username': self.username,
                'password': self.password,
                'auth_type_password': 'Sign in',
            },
            allow_redirects=False
        )

        code_redirect = response._next.url
        code_query = requests.utils.urlparse(code_redirect).query
        code = dict(x.split('=') for x in code_query.split('&'))['code']
        return code

    token = property(__get_token, __set_token)
