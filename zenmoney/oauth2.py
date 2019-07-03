#!/usr/bin/env python

'''
Get oauth token for further requests to the API

You need to get a consumer_key and consumer_secret from
http://api.zenmoney.ru/consumer.html
and use your username and password then.
'''
import requests
from . import API_URL, ZenMoneyException


class OAuth2(object):

    uri_auth = API_URL + '/oauth2/authorize/'
    uri_token = API_URL + '/oauth2/token/'
    uri_redirect = 'notscheme://localhost/'

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
        response = self.__post(
            self.uri_token,
            data={
                'grant_type': 'authorization_code',
                'client_id': self.consumer_key,
                'client_secret': self.consumer_secret,
                'code': code,
                'redirect_uri': self.uri_redirect,
            }
        )

        self._token = response.json()['access_token']
        self._token_response = response.json()

    def _get_code(self):
        '''
        Get auth cookie, authorize user and then get the code for token
        '''
        self.s.get(
            self.uri_auth,
            params={
                'response_type': 'code',
                'client_id': self.consumer_key,
                'redirect_uri': self.uri_redirect,
            }
        )
        response = self.__post(
            self.uri_auth,
            json={
                'username': self.username,
                'password': self.password,
                'auth_type_password': 'Sign in',
            },
            allow_redirects=False
        )

        code_redirect = response._next.url
        code_query = requests.utils.urlparse(code_redirect).query
        code_dict = dict(x.split('=') for x in code_query.split('&'))
        if not code_dict.get('code', False):
            raise ZenMoneyException(
                'User authorization redirect url {} does not contain '
                "'code' parameter".format(
                    code_redirect
                ),
                response=response,
            )
        return code_dict.get('code')

    token = property(__get_token, __set_token)

    def __post(self, uri: str, **kwargs):
        '''
        Wrapper for request.post, which raises exception on non ok results
        '''
        response = self.s.post(uri, **kwargs)
        if not response.ok:
            raise ZenMoneyException(
                'POST request to {} wasn\'t successful, code={}'
                .format(uri, response.status_code),
                uri=uri, response=response
            )
        return response
