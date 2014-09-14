# coding: utf-8

from __future__ import unicode_literals

import mock
import requests

from digitalocean import ClientV2


class TestRegions:

    @mock.patch.object(requests, 'get')
    def test_all(self, get):
        response = requests.Response()
        response._content = b'''{
          "regions": [
            {
              "slug": "nyc1",
              "name": "New York",
              "sizes": [

              ],
              "available": false,
              "features": [
                "virtio",
                "private_networking",
                "backups",
                "ipv6"
              ]
            },
            {
              "slug": "sfo1",
              "name": "San Francisco",
              "sizes": [
                "1gb",
                "512mb"
              ],
              "available": true,
              "features": [
                "virtio",
                "backups"
              ]
            },
            {
              "slug": "ams1",
              "name": "Amsterdam",
              "sizes": [
                "1gb",
                "512mb"
              ],
              "available": true,
              "features": [
                "virtio",
                "backups"
              ]
            }
          ],
          "meta": {
            "total": 3
          }
        }'''
        get.return_value = response

        client = ClientV2(token='token')
        data = client.regions.all()

        get.assert_called_with(
            'https://api.digitalocean.com/v2/regions',
            headers={'Authorization': 'Bearer token'},
            params={})

        assert len(data['regions']) == 3
        assert data['meta']['total'] == 3
        assert data['regions'][0]['slug'] == 'nyc1'
        assert data['regions'][0]['name'] == 'New York'
        assert data['regions'][0]['sizes'] == []
        assert data['regions'][0]['available'] is False
        assert data['regions'][0]['features'] == [
            "virtio",
            "private_networking",
            "backups",
            "ipv6"
        ]
