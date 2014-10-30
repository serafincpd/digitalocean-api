# coding: utf-8

from __future__ import unicode_literals

import mock
import requests

from digitalocean import ClientV2


class TestKeys:

    @mock.patch.object(requests, 'get')
    def test_all(self, get):
        response = requests.Response()
        response._content = b'''{
          "ssh_keys": [
            {
              "id": 1,
              "fingerprint": "fingerprint",
              "public_key": "ssh-rsa public_key",
              "name": "Example Key"
            }
          ],
          "meta": {
            "total": 1
          }
        }'''

        get.return_value = response

        client = ClientV2(token='token')
        data = client.keys.all()

        get.assert_called_with(
            'https://api.digitalocean.com/v2/account/keys',
            headers={'Authorization': 'Bearer token'},
            params={})

        assert len(data['ssh_keys']) == 1
        assert data['meta']['total'] == 1
        assert data['ssh_keys'][0]['id'] == 1
        assert data['ssh_keys'][0]['fingerprint'] == 'fingerprint'
        assert data['ssh_keys'][0]['public_key'] == 'ssh-rsa public_key'
        assert data['ssh_keys'][0]['name'] == 'Example Key'

    @mock.patch.object(requests, 'post')
    def test_create(self, post):
        response = requests.Response()
        response._content = b'''{
          "ssh_key": {
            "id": 2,
            "fingerprint": "fingerprint",
            "public_key": "ssh-rsa example",
            "name": "Example Key"
          }
        }'''

        post.return_value = response

        client = ClientV2(token='token')
        data = client.keys.create(name='Example Key',
                                  public_key='ssh-rsa example')

        post.assert_called_with(
            'https://api.digitalocean.com/v2/account/keys',
            headers={'content-type': 'application/json',
                     'Authorization': 'Bearer token'},
            data='{"public_key": "ssh-rsa example", "name": "Example Key"}')

        assert len(data) == 1
        assert data['ssh_key']['id'] == 2
        assert data['ssh_key']['fingerprint'] == 'fingerprint'
        assert data['ssh_key']['public_key'] == 'ssh-rsa example'
        assert data['ssh_key']['name'] == 'Example Key'

    @mock.patch.object(requests, 'get')
    def test_get(self, get):
        response = requests.Response()
        response._content = b'''{
          "ssh_key": {
            "id": 2,
            "fingerprint": "fingerprint",
            "public_key": "ssh-rsa example",
            "name": "Example Key"
          }
        }'''

        get.return_value = response

        client = ClientV2(token='token')
        data = client.keys.get(key_id=2)

        get.assert_called_with(
            'https://api.digitalocean.com/v2/account/keys/2',
            headers={'Authorization': 'Bearer token'},
            params={})

        assert len(data) == 1
        assert data['ssh_key']['id'] == 2
        assert data['ssh_key']['fingerprint'] == 'fingerprint'
        assert data['ssh_key']['public_key'] == 'ssh-rsa example'
        assert data['ssh_key']['name'] == 'Example Key'

    @mock.patch.object(requests, 'put')
    def test_update(self, put):
        response = requests.Response()
        response._content = b'''{
          "ssh_key": {
            "id": 4,
            "fingerprint": "fingerprint",
            "public_key": "ssh-rsa example",
            "name": "New Name"
          }
        }'''

        put.return_value = response

        client = ClientV2(token='token')
        data = client.keys.update(key_id=4, name='New Name')

        put.assert_called_with(
            'https://api.digitalocean.com/v2/account/keys/4',
            headers={'content-type': 'application/json',
                     'Authorization': 'Bearer token'},
            params={'name': 'New Name'})

        assert len(data) == 1
        assert data['ssh_key']['id'] == 4
        assert data['ssh_key']['fingerprint'] == 'fingerprint'
        assert data['ssh_key']['public_key'] == 'ssh-rsa example'
        assert data['ssh_key']['name'] == 'New Name'

    @mock.patch.object(requests, 'delete')
    def test_delete(self, delete):
        response = requests.Response()
        response._content = b''
        response.status_code = 204

        delete.return_value = response

        client = ClientV2(token='token')
        data = client.keys.delete(key_id=4)

        delete.assert_called_with(
            'https://api.digitalocean.com/v2/account/keys/4',
            headers={'content-type': 'application/x-www-form-urlencoded',
                     'Authorization': 'Bearer token'},
            params={})

        assert data == ''

        data = client.keys.delete(key_id='fingerprint')

        delete.assert_called_with(
            'https://api.digitalocean.com/v2/account/keys/fingerprint',
            headers={'content-type': 'application/x-www-form-urlencoded',
                     'Authorization': 'Bearer token'},
            params={})

        assert data == ''
