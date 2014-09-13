# coding: utf-8

from digitalocean.api.baseapi import BaseAPI


class Keys(BaseAPI):

    def all(self):
        "List all Keys"

        return self.request('account/keys', 'GET')

    def create(self, name, public_key):
        "Create a new Key"

        params = {'name': name, 'public_key': public_key}
        return self.request('account/keys', 'POST', params=params)

    def get(self, key_id):
        "Retrieve an existing Key by Id or Fingerprint"

        return self.request('account/keys/{}'.format(key_id), 'GET')

    def update(self, key_id, name):
        "Update an existing Key by Id or Fingerprint"

        params = {'name': name}
        return self.request(
            'account/keys/{}'.format(key_id), 'PUT', params=params)

    def delete(self, key_id):
        "Destroy an existing Key by Id or Fingerprint"

        return self.request('account/keys/{}'.format(key_id), 'DELETE')
