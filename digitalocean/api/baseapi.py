# coding: utf-8

from __future__ import unicode_literals

import json
from urlparse import urljoin

import requests
from digitalocean.api.exceptions import (
    JSONDecodeError,
    NoTokenProvided,
    ResponseError,
    RequestError
)


class BaseAPI(object):

    endpoint = 'https://api.digitalocean.com/v2/'

    def __init__(self, token=None):
        self.token = token

    def __str__(self):
        return b'<{:s} at {:#x}>'.format(type(self).__name__, id(self))

    def __unicode__(self):
        return '<{:s} at {:#x}>'.format(type(self).__name__, id(self))

    def __set_content_type(self, headers, ctype):
        headers.update({'content-type': ctype})

    def __set_authorization(self, headers):
        if not self.token:
            raise NoTokenProvided()

        headers.update({'Authorization': 'Bearer {:s}'.format(self.token)})

    def __get(self, url, params, headers):
        return requests.get(url, params=params, headers=headers)

    def __post(self, url, params, headers):
        self.__set_content_type(headers, 'application/json')
        return requests.post(url, data=json.dumps(params), headers=headers)

    def __put(self, url, params, headers):
        self.__set_content_type(headers, 'application/json')
        return requests.put(url, params=params, headers=headers)

    def __delete(self, url, params, headers):
        self.__set_content_type(headers, 'application/x-www-form-urlencoded')
        return requests.delete(url, params=params, headers=headers)

    def __head(self, url, params, headers):
        return requests.head(url, headers=headers)

    def __request(self, url, method, params, headers=None):
        headers = headers or {}

        METHODS = {
            'get': self.__get,
            'post': self.__post,
            'put': self.__put,
            'delete': self.__delete,
            'head': self.__head
        }

        self.__set_authorization(headers)

        request_method = METHODS[method.lower()]
        url = urljoin(self.endpoint, url)

        return request_method(url, params=params, headers=headers)

    def request(self, url, method, params=None):
        params = params or {}

        response = self.__request(url, method, params)

        if response.status_code == 204:
            json = ''
        else:
            try:
                json = response.json()
            except ValueError:
                raise JSONDecodeError()

            if not response.ok:
                if response.status_code >= 500:
                    raise ResponseError(
                        'Server did not respond. {:d} {:s}'.format(
                            response.status_code, response.reason))

                raise RequestError('{:d} {:s}. Message: {:s}'.format(
                    response.status_code, response.reason, json['message']))

        return json
