# coding: utf-8

from digitalocean.api.baseapi import BaseAPI


class Regions(BaseAPI):

    def all(self):
        "List all Regions"

        return self.request('regions', 'GET')
