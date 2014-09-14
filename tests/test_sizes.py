# coding: utf-8

from __future__ import unicode_literals

import mock
import requests

from digitalocean import ClientV2


class TestSizes:

    @mock.patch.object(requests, 'get')
    def test_all(self, get):
        response = requests.Response()
        response._content = b'''{
          "slug": "512mb",
          "memory": 512,
          "vcpus": 1,
          "disk": 20,
          "transfer": 2,
          "price_monthly": 5.0,
          "price_hourly": 0.00744,
          "regions": [
            "nyc1",
            "br1",
            "sfo1",
            "ams4"
          ]
        }'''
        get.return_value = response

        client = ClientV2(token='token')
        data = client.sizes.all()

        get.assert_called_with(
            'https://api.digitalocean.com/v2/sizes',
            headers={'Authorization': 'Bearer token'},
            params={})

        assert data['slug'] == '512mb'
        assert data['memory'] == 512
        assert data['vcpus'] == 1
        assert data['disk'] == 20
        assert data['transfer'] == 2
        assert data['price_monthly'] == 5.0
        assert data['price_hourly'] == 0.00744
        assert data['regions'] == ["nyc1", "br1", "sfo1", "ams4"]
