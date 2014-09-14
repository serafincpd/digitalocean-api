# coding: utf-8

from __future__ import unicode_literals

import mock
import requests

from digitalocean import ClientV2


class TestActions:

    @mock.patch.object(requests, 'get')
    def test_all(self, get):
        response = requests.Response()
        response._content = b'''{
          "actions": [
            {
              "id": 1,
              "status": "in-progress",
              "type": "test",
              "started_at": "2014-09-05T02:01:57Z",
              "completed_at": null,
              "resource_id": null,
              "resource_type": "backend",
              "region": "nyc1"
            }
          ],
          "meta": {
            "total": 1
          }
        }'''

        get.return_value = response

        client = ClientV2(token='token')
        data = client.actions.all()

        get.assert_called_with(
            'https://api.digitalocean.com/v2/actions',
            headers={'Authorization': 'Bearer token'},
            params={})

        assert len(data['actions']) == 1
        assert data['meta']['total'] == 1
        assert data['actions'][0]['id'] == 1
        assert data['actions'][0]['status'] == 'in-progress'
        assert data['actions'][0]['type'] == 'test'
        assert data['actions'][0]['started_at'] == '2014-09-05T02:01:57Z'
        assert data['actions'][0]['completed_at'] is None
        assert data['actions'][0]['resource_id'] is None
        assert data['actions'][0]['resource_type'] == 'backend'
        assert data['actions'][0]['region'] == 'nyc1'

    @mock.patch.object(requests, 'get')
    def test_get(self, get):
        response = requests.Response()
        response._content = b'''{
          "action": {
            "id": 2,
            "status": "in-progress",
            "type": "test",
            "started_at": "2014-09-05T02:01:58Z",
            "completed_at": null,
            "resource_id": null,
            "resource_type": "backend",
            "region": "nyc1"
          }
        }'''

        get.return_value = response

        client = ClientV2(token='token')
        data = client.actions.get(action_id=2)

        get.assert_called_with(
            'https://api.digitalocean.com/v2/actions/2',
            headers={'Authorization': 'Bearer token'},
            params={})

        assert len(data) == 1
        assert data['action']['id'] == 2
        assert data['action']['status'] == 'in-progress'
        assert data['action']['type'] == 'test'
        assert data['action']['started_at'] == '2014-09-05T02:01:58Z'
        assert data['action']['completed_at'] is None
        assert data['action']['resource_id'] is None
        assert data['action']['resource_type'] == 'backend'
        assert data['action']['region'] == 'nyc1'
