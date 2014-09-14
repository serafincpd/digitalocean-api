# coding: utf-8

from __future__ import unicode_literals

import mock
import requests

from digitalocean import ClientV2


class TestDomains:

    @mock.patch.object(requests, 'get')
    def test_all(self, get):
        response = requests.Response()
        response._content = b'''{
          "domains": [
            {
              "name": "example.com",
              "ttl": 1800,
              "zone_file": "Example zone file text..."
            }
          ],
          "meta": {
            "total": 1
          }
        }'''

        get.return_value = response

        client = ClientV2(token='token')
        data = client.domains.all()

        get.assert_called_with(
            'https://api.digitalocean.com/v2/domains',
            headers={'Authorization': 'Bearer token'},
            params={})

        assert len(data['domains']) == 1
        assert data['meta']['total'] == 1
        assert data['domains'][0]['name'] == 'example.com'
        assert data['domains'][0]['ttl'] == 1800
        assert data['domains'][0]['zone_file'] == 'Example zone file text...'

    @mock.patch.object(requests, 'post')
    def test_create(self, post):
        response = requests.Response()
        response._content = b'''{
          "domain": {
            "name": "example.com",
            "ttl": 1800,
            "zone_file": null
          }
        }'''

        post.return_value = response

        client = ClientV2(token='token')
        data = client.domains.create(name='example.com',
                                     ip_address='127.0.0.1')

        post.assert_called_with(
            'https://api.digitalocean.com/v2/domains',
            headers={'content-type': 'application/json',
                     'Authorization': 'Bearer token'},
            params={'name': 'example.com', 'ip_address': '127.0.0.1'})

        assert len(data) == 1
        assert data['domain']['name'] == 'example.com'
        assert data['domain']['ttl'] == 1800
        assert data['domain']['zone_file'] is None

    @mock.patch.object(requests, 'get')
    def test_get(self, get):
        response = requests.Response()
        response._content = b'''{
          "domain": {
            "name": "example.com",
            "ttl": 1800,
            "zone_file": "Example zone file text..."
          }
        }'''

        get.return_value = response

        client = ClientV2(token='token')
        data = client.domains.get(domain_id='example.com')

        get.assert_called_with(
            'https://api.digitalocean.com/v2/domains/example.com',
            headers={'Authorization': 'Bearer token'},
            params={})

        assert len(data) == 1
        assert data['domain']['name'] == 'example.com'
        assert data['domain']['ttl'] == 1800
        assert data['domain']['zone_file'] == 'Example zone file text...'

    @mock.patch.object(requests, 'delete')
    def test_delete(self, delete):
        response = requests.Response()
        response._content = b''
        response.status_code = 204

        delete.return_value = response

        client = ClientV2(token='token')
        data = client.domains.delete(domain_id='example.com')

        delete.assert_called_with(
            'https://api.digitalocean.com/v2/domains/example.com',
            headers={'content-type': 'application/x-www-form-urlencoded',
                     'Authorization': 'Bearer token'},
            params={})

        assert data == ''

    @mock.patch.object(requests, 'get')
    def test_list_domain_records(self, get):
        response = requests.Response()
        response._content = b'''{
          "domain_records": [
            {
              "id": 1,
              "type": "A",
              "name": "@",
              "data": "8.8.8.8",
              "priority": null,
              "port": null,
              "weight": null
            },
            {
              "id": 2,
              "type": "NS",
              "name": null,
              "data": "NS1.DIGITALOCEAN.COM.",
              "priority": null,
              "port": null,
              "weight": null
            },
            {
              "id": 3,
              "type": "NS",
              "name": null,
              "data": "NS2.DIGITALOCEAN.COM.",
              "priority": null,
              "port": null,
              "weight": null
            },
            {
              "id": 4,
              "type": "NS",
              "name": null,
              "data": "NS3.DIGITALOCEAN.COM.",
              "priority": null,
              "port": null,
              "weight": null
            },
            {
              "id": 5,
              "type": "CNAME",
              "name": "example",
              "data": "@",
              "priority": null,
              "port": null,
              "weight": null
            }
          ],
          "meta": {
            "total": 5
          }
        }'''

        get.return_value = response

        client = ClientV2(token='token')
        data = client.domains.list_domain_records(domain_id='example.com')

        get.assert_called_with(
            'https://api.digitalocean.com/v2/domains/example.com/records',
            headers={'Authorization': 'Bearer token'},
            params={})

        assert len(data['domain_records']) == 5
        assert data['domain_records'][0]['id'] == 1
        assert data['domain_records'][0]['type'] == 'A'
        assert data['domain_records'][1]['id'] == 2
        assert data['domain_records'][1]['type'] == 'NS'
        assert data['domain_records'][2]['id'] == 3
        assert data['domain_records'][2]['type'] == 'NS'
        assert data['domain_records'][3]['id'] == 4
        assert data['domain_records'][3]['type'] == 'NS'
        assert data['domain_records'][4]['id'] == 5
        assert data['domain_records'][4]['type'] == 'CNAME'

    @mock.patch.object(requests, 'post')
    def test_create_domain_record(self, post):
        response = requests.Response()
        response._content = b'''{
          "domain_record": {
            "id": 16,
            "type": "AAAA",
            "name": "subdomain",
            "data": "2001:db8::ff00:42:8329",
            "priority": null,
            "port": null,
            "weight": null
          }
        }'''

        post.return_value = response

        client = ClientV2(token='token')
        data = client.domains.create_domain_record(
            domain_id=123, name='subdomain',
            data='2001:db8::ff00:42:8329', rtype='AAAA')

        post.assert_called_with(
            'https://api.digitalocean.com/v2/domains/123/records',
            headers={'content-type': 'application/json',
                     'Authorization': 'Bearer token'},
            params={'name': 'subdomain',
                    'data': '2001:db8::ff00:42:8329', 'type': 'AAAA'})

        assert len(data) == 1
        assert data['domain_record']['id'] == 16
        assert data['domain_record']['type'] == 'AAAA'
        assert data['domain_record']['name'] == 'subdomain'
        assert data['domain_record']['data'] == '2001:db8::ff00:42:8329'

    @mock.patch.object(requests, 'get')
    def test_get_domain_record(self, get):
        response = requests.Response()
        response._content = b'''{
          "domain_record": {
            "id": 10,
            "type": "CNAME",
            "name": "example",
            "data": "@",
            "priority": null,
            "port": null,
            "weight": null
          }
        }'''

        get.return_value = response

        client = ClientV2(token='token')
        data = client.domains.get_domain_record(domain_id='example.com',
                                                record_id=10)

        get.assert_called_with(
            'https://api.digitalocean.com/v2/domains/example.com/records/10',
            headers={'Authorization': 'Bearer token'},
            params={})

        assert len(data) == 1
        assert data['domain_record']['id'] == 10

    @mock.patch.object(requests, 'delete')
    def test_delete_domain_record(self, delete):
        response = requests.Response()
        response._content = b''
        response.status_code = 204

        delete.return_value = response

        client = ClientV2(token='token')
        data = client.domains.delete_domain_record(domain_id='example.com',
                                                   record_id=10)

        delete.assert_called_with(
            'https://api.digitalocean.com/v2/domains/example.com/records/10',
            headers={'content-type': 'application/x-www-form-urlencoded',
                     'Authorization': 'Bearer token'},
            params={})

        assert data == ''

    @mock.patch.object(requests, 'put')
    def test_update_domain_record(self, put):
        response = requests.Response()
        response._content = b'''{
          "domain_record": {
            "id": 26,
            "type": "CNAME",
            "name": "new_name",
            "data": "@",
            "priority": null,
            "port": null,
            "weight": null
          }
        }'''

        put.return_value = response

        client = ClientV2(token='token')
        data = client.domains.update_domain_record(domain_id='example.com',
                                                   record_id=26,
                                                   name='new_name')

        put.assert_called_with(
            'https://api.digitalocean.com/v2/domains/example.com/records/26',
            headers={'content-type': 'application/json',
                     'Authorization': 'Bearer token'},
            params={'name': 'new_name'})

        assert len(data) == 1
        assert data['domain_record']['id'] == 26
        assert data['domain_record']['name'] == 'new_name'
