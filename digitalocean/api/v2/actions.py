# coding: utf-8

from digitalocean.api.baseapi import BaseAPI


class Actions(BaseAPI):

    def all(self):
        "List all Actions"

        return self.request('actions', 'GET')

    def get(self, action_id):
        "Retrieve an existing Action"

        return self.request('actions/{}'.format(action_id), 'GET')
