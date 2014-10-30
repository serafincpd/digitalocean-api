# coding: utf-8

from __future__ import unicode_literals

import mock
import requests

from digitalocean import ClientV2


class TestImages:

    @mock.patch.object(requests, 'get')
    def test_all(self, get):
        response = requests.Response()
        response._content = b'''{
          "images": [
            {
              "id": 119192817,
              "name": "Ubuntu 13.04",
              "distribution": "ubuntu",
              "slug": "ubuntu1304",
              "public": true,
              "regions": [
                "nyc1"
              ],
              "created_at": "2014-09-05T02:02:08Z"
            },
            {
              "id": 449676376,
              "name": "Ubuntu 13.04",
              "distribution": "ubuntu",
              "slug": "ubuntu1404",
              "public": true,
              "regions": [
                "nyc1"
              ],
              "created_at": "2014-09-05T02:02:08Z"
            }
          ],
          "meta": {
            "total": 2
          }
        }'''

        get.return_value = response

        client = ClientV2(token='token')
        data = client.images.all()

        get.assert_called_with(
            'https://api.digitalocean.com/v2/images',
            headers={'Authorization': 'Bearer token'},
            params={})

        assert len(data['images']) == 2
        assert data['meta']['total'] == 2
        assert data['images'][0]['id'] == 119192817
        assert data['images'][0]['name'] == 'Ubuntu 13.04'
        assert data['images'][0]['distribution'] == 'ubuntu'
        assert data['images'][0]['slug'] == 'ubuntu1304'
        assert data['images'][0]['public'] is True
        assert data['images'][0]['regions'] == ['nyc1']
        assert data['images'][0]['created_at'] == '2014-09-05T02:02:08Z'

    @mock.patch.object(requests, 'get')
    def test_get(self, get):
        response = requests.Response()
        response._content = b'''{
          "image": {
            "id": 449676376,
            "name": "Ubuntu 13.04",
            "distribution": "ubuntu",
            "slug": "ubuntu1404",
            "public": true,
            "regions": [
              "nyc1"
            ],
            "created_at": "2014-09-05T02:02:08Z"
          }
        }'''

        get.return_value = response

        client = ClientV2(token='token')
        data = client.images.get(image_id=449676376)

        get.assert_called_with(
            'https://api.digitalocean.com/v2/images/449676376',
            headers={'Authorization': 'Bearer token'},
            params={})

        assert len(data) == 1
        assert data['image']['id'] == 449676376
        assert data['image']['name'] == 'Ubuntu 13.04'
        assert data['image']['distribution'] == 'ubuntu'
        assert data['image']['slug'] == 'ubuntu1404'
        assert data['image']['public'] is True
        assert data['image']['regions'] == ['nyc1']
        assert data['image']['created_at'] == '2014-09-05T02:02:08Z'

        data = client.images.get(image_id='ubuntu1404')

        get.assert_called_with(
            'https://api.digitalocean.com/v2/images/ubuntu1404',
            headers={'Authorization': 'Bearer token'},
            params={})

        assert len(data) == 1
        assert data['image']['id'] == 449676376
        assert data['image']['name'] == 'Ubuntu 13.04'
        assert data['image']['distribution'] == 'ubuntu'
        assert data['image']['slug'] == 'ubuntu1404'
        assert data['image']['public'] is True
        assert data['image']['regions'] == ['nyc1']
        assert data['image']['created_at'] == '2014-09-05T02:02:08Z'

    @mock.patch.object(requests, 'delete')
    def test_delete(self, delete):
        response = requests.Response()
        response._content = b''
        response.status_code = 204

        delete.return_value = response

        client = ClientV2(token='token')
        data = client.images.delete(image_id=449676376)

        delete.assert_called_with(
            'https://api.digitalocean.com/v2/images/449676376',
            headers={'content-type': 'application/x-www-form-urlencoded',
                     'Authorization': 'Bearer token'},
            params={})

        assert data == ''

    @mock.patch.object(requests, 'put')
    def test_update(self, put):
        response = requests.Response()
        response._content = b'''{
          "image": {
            "id": 449676394,
            "name": "New Image Name",
            "distribution": null,
            "slug": null,
            "public": false,
            "regions": [
              "region--3"
            ],
            "created_at": "2014-09-05T02:02:09Z"
          }
        }'''

        put.return_value = response

        client = ClientV2(token='token')
        data = client.images.update(image_id=449676394, name='New Image Name')

        put.assert_called_with(
            'https://api.digitalocean.com/v2/images/449676394',
            headers={'content-type': 'application/json',
                     'Authorization': 'Bearer token'},
            params={'name': 'New Image Name'})

        assert len(data) == 1
        assert data['image']['id'] == 449676394
        assert data['image']['name'] == 'New Image Name'
        assert data['image']['distribution'] is None
        assert data['image']['slug'] is None
        assert data['image']['public'] is False
        assert data['image']['regions'] == ['region--3']
        assert data['image']['created_at'] == '2014-09-05T02:02:09Z'

    @mock.patch.object(requests, 'post')
    def test_transfer(self, post):
        response = requests.Response()
        response._content = b'''{
          "action": {
            "id": 23,
            "status": "in-progress",
            "type": "transfer",
            "started_at": "2014-09-05T02:02:08Z",
            "completed_at": null,
            "resource_id": 449676391,
            "resource_type": "image",
            "region": "nyc1"
          }
        }'''

        post.return_value = response

        client = ClientV2(token='token')
        data = client.images.transfer(image_id=449676391, region='nyc1')

        post.assert_called_with(
            'https://api.digitalocean.com/v2/images/449676391/actions',
            headers={'content-type': 'application/json',
                     'Authorization': 'Bearer token'},
            data='{"region": "nyc1", "type": "transfer"}')

        assert len(data) == 1
        assert data['action']['id'] == 23
        assert data['action']['status'] == 'in-progress'
        assert data['action']['type'] == 'transfer'
        assert data['action']['started_at'] == '2014-09-05T02:02:08Z'
        assert data['action']['completed_at'] is None
        assert data['action']['resource_id'] == 449676391
        assert data['action']['resource_type'] == 'image'
        assert data['action']['region'] == 'nyc1'

    @mock.patch.object(requests, 'get')
    def test_get_image_action(self, get):
        response = requests.Response()
        response._content = b'''{
          "action": {
            "id": 22,
            "status": "in-progress",
            "type": "transfer",
            "started_at": "2014-09-05T02:02:07Z",
            "completed_at": null,
            "resource_id": 449676390,
            "resource_type": "image",
            "region": "nyc1"
          }
        }'''

        get.return_value = response

        client = ClientV2(token='token')
        data = client.images.get_image_action(image_id=449676390, action_id=22)

        get.assert_called_with(
            'https://api.digitalocean.com/v2/images/449676390/actions/22',
            headers={'Authorization': 'Bearer token'},
            params={})

        assert len(data) == 1
        assert data['action']['id'] == 22
        assert data['action']['status'] == 'in-progress'
        assert data['action']['type'] == 'transfer'
        assert data['action']['started_at'] == '2014-09-05T02:02:07Z'
        assert data['action']['completed_at'] is None
        assert data['action']['resource_id'] == 449676390
        assert data['action']['resource_type'] == 'image'
        assert data['action']['region'] == 'nyc1'
