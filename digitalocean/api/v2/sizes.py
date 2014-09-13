# coding: utf-8

from digitalocean.api.baseapi import BaseAPI


class Sizes(BaseAPI):

    def all(self):
        "List all Sizes"

        return self.request('sizes', 'GET')
