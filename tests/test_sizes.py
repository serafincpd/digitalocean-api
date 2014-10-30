# coding: utf-8

from __future__ import unicode_literals

import mock
import requests

from digitalocean import ClientV2


class TestSizes:

    @mock.patch.object(requests, 'get')
    def test_all(self, get):
        response = requests.Response()
        response._content = b'''
        {
          "sizes": [
            {
              "slug": "512mb",
              "memory": 512,
              "vcpus": 1,
              "disk": 20,
              "transfer": 1,
              "price_monthly": 5.0,
              "price_hourly": 0.00744,
              "regions": [
                "nyc1",
                "sfo1",
                "ams1"
              ]
            },
            {
              "slug": "1gb",
              "memory": 1024,
              "vcpus": 2,
              "disk": 30,
              "transfer": 2,
              "price_monthly": 10.0,
              "price_hourly": 0.01488,
              "regions": [
                "nyc1",
                "sfo1",
                "ams1"
              ]
            }
          ],
          "meta": {
            "total": 2
          }
        }'''
        get.return_value = response

        client = ClientV2(token='token')
        data = client.sizes.all()

        get.assert_called_with(
            'https://api.digitalocean.com/v2/sizes',
            headers={'Authorization': 'Bearer token'},
            params={})

        assert data['sizes'][0]['slug'] == '512mb'
        assert data['sizes'][0]['memory'] == 512
        assert data['sizes'][0]['vcpus'] == 1
        assert data['sizes'][0]['disk'] == 20
        assert data['sizes'][0]['transfer'] == 1
        assert data['sizes'][0]['price_monthly'] == 5.0
        assert data['sizes'][0]['price_hourly'] == 0.00744
        assert data['sizes'][0]['regions'] == ["nyc1", "sfo1", "ams1"]
