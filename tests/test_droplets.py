# coding: utf-8

from __future__ import unicode_literals

import mock
import requests

from digitalocean import ClientV2


class TestDroplets:

    @mock.patch.object(requests, 'get')
    def test_all(self, get):
        response = requests.Response()
        response._content = b'''{
          "droplets": [
            {
              "id": 19,
              "name": "test.example.com",
              "memory": 512,
              "vcpus": 1,
              "disk": 20,
              "region": {
                "slug": "nyc1",
                "name": "New York",
                "sizes": [
                  "1gb",
                  "512mb"
                ],
                "available": true,
                "features": [
                  "virtio",
                  "private_networking",
                  "backups",
                  "ipv6"
                ]
              },
              "image": {
                "id": 119192817,
                "name": "Ubuntu 13.04",
                "distribution": "ubuntu",
                "slug": "ubuntu1304",
                "public": true,
                "regions": [
                  "nyc1"
                ],
                "created_at": "2014-09-05T02:02:05Z"
              },
              "size": {
                "slug": "512mb",
                "transfer": 1,
                "price_monthly": 5.0,
                "price_hourly": 0.00744
              },
              "locked": false,
              "status": "active",
              "networks": {
                "v4": [
                  {
                    "ip_address": "127.0.0.19",
                    "netmask": "255.255.255.0",
                    "gateway": "127.0.0.20",
                    "type": "public"
                  }
                ],
                "v6": [
                  {
                    "ip_address": "2001::13",
                    "cidr": 124,
                    "gateway": "2400:6180:0000:00D0:0000:0000:0009:7000",
                    "type": "public"
                  }
                ]
              },
              "kernel": {
                "id": 485432985,
                "name": "DO-recovery-static-fsck",
                "version": "3.8.0-25-generic"
              },
              "created_at": "2014-09-05T02:02:05Z",
              "features": [
                "ipv6"
              ],
              "backup_ids": [

              ],
              "snapshot_ids": [

              ]
            }
          ],
          "meta": {
            "total": 1
          }
        }'''

        get.return_value = response

        client = ClientV2(token='token')
        data = client.droplets.all()

        get.assert_called_with(
            'https://api.digitalocean.com/v2/droplets',
            headers={'Authorization': 'Bearer token'},
            params={})

        assert len(data['droplets']) == 1
        assert data['meta']['total'] == 1
        assert data['droplets'][0]['id'] == 19
        assert data['droplets'][0]['name'] == 'test.example.com'
        assert data['droplets'][0]['memory'] == 512
        assert data['droplets'][0]['vcpus'] == 1
        assert data['droplets'][0]['disk'] == 20
        assert 'region' in data['droplets'][0]
        assert 'image' in data['droplets'][0]
        assert 'size' in data['droplets'][0]
        assert 'locked' in data['droplets'][0]
        assert 'status' in data['droplets'][0]
        assert 'networks' in data['droplets'][0]
        assert 'kernel' in data['droplets'][0]
        assert 'created_at' in data['droplets'][0]
        assert 'features' in data['droplets'][0]
        assert 'backup_ids' in data['droplets'][0]
        assert 'snapshot_ids' in data['droplets'][0]

    @mock.patch.object(requests, 'get')
    def test_list_droplet_kernels(self, get):
        response = requests.Response()
        response._content = b'''{
          "kernels": [
            {
              "id": 61833229,
              "name": "Ubuntu 14.04 x32",
              "version": "3.13.0-24-generic"
            },
            {
              "id": 485432972,
              "name": "Ubuntu 14.04 x64",
              "version": "3.13.0-24-generic"
            }
          ],
          "meta": {
            "total": 2
          }
        }'''

        get.return_value = response

        client = ClientV2(token='token')
        data = client.droplets.list_droplet_kernels(droplet_id=123)

        get.assert_called_with(
            'https://api.digitalocean.com/v2/droplets/123/kernels',
            headers={'Authorization': 'Bearer token'},
            params={})

        assert len(data['kernels']) == 2
        assert data['meta']['total'] == 2
        assert data['kernels'][0]['id'] == 61833229
        assert data['kernels'][0]['name'] == 'Ubuntu 14.04 x32'
        assert data['kernels'][0]['version'] == '3.13.0-24-generic'

    @mock.patch.object(requests, 'get')
    def test_get_droplet_snapshots(self, get):
        response = requests.Response()
        response._content = b'''{
          "snapshots": [

          ],
          "meta": {
            "total": 0
          }
        }'''

        get.return_value = response

        client = ClientV2(token='token')
        data = client.droplets.get_droplet_snapshots(droplet_id=123)

        get.assert_called_with(
            'https://api.digitalocean.com/v2/droplets/123/snapshots',
            headers={'Authorization': 'Bearer token'},
            params={})

        assert len(data['snapshots']) == 0
        assert data['meta']['total'] == 0

    @mock.patch.object(requests, 'get')
    def test_get_droplet_backups(self, get):
        response = requests.Response()
        response._content = b'''{
          "backups": [

          ],
          "meta": {
            "total": 0
          }
        }'''

        get.return_value = response

        client = ClientV2(token='token')
        data = client.droplets.get_droplet_backups(droplet_id=123)

        get.assert_called_with(
            'https://api.digitalocean.com/v2/droplets/123/backups',
            headers={'Authorization': 'Bearer token'},
            params={})

        assert len(data['backups']) == 0
        assert data['meta']['total'] == 0

    @mock.patch.object(requests, 'get')
    def test_get_droplet_actions(self, get):
        response = requests.Response()
        response._content = b'''{
          "actions": [
            {
              "id": 19,
              "status": "in-progress",
              "type": "create",
              "started_at": "2014-09-05T02:02:06Z",
              "completed_at": null,
              "resource_id": 123,
              "resource_type": "droplet",
              "region": "nyc1"
            }
          ],
          "meta": {
            "total": 1
          }
        }'''

        get.return_value = response

        client = ClientV2(token='token')
        data = client.droplets.get_droplet_actions(droplet_id=123)

        get.assert_called_with(
            'https://api.digitalocean.com/v2/droplets/123/actions',
            headers={'Authorization': 'Bearer token'},
            params={})

        assert len(data['actions']) == 1
        assert data['meta']['total'] == 1
        assert data['actions'][0]['id'] == 19
        assert data['actions'][0]['status'] == 'in-progress'
        assert data['actions'][0]['type'] == 'create'
        assert data['actions'][0]['started_at'] == '2014-09-05T02:02:06Z'
        assert data['actions'][0]['completed_at'] is None
        assert data['actions'][0]['resource_id'] == 123
        assert data['actions'][0]['resource_type'] == 'droplet'
        assert data['actions'][0]['region'] == 'nyc1'

    @mock.patch.object(requests, 'post')
    def test_create(self, post):
        response = requests.Response()
        response._content = b'''{
          "droplet": {
            "id": 25,
            "name": "My-Droplet",
            "memory": 512,
            "vcpus": 1,
            "disk": 20,
            "region": {
              "slug": "nyc1",
              "name": "New York",
              "sizes": [
                "1gb",
                "512mb"
              ],
              "available": true,
              "features": [
                "virtio",
                "private_networking",
                "backups",
                "ipv6"
              ]
            },
            "image": {
              "id": 449676389,
              "name": "Ubuntu 13.04",
              "distribution": "ubuntu",
              "slug": null,
              "public": true,
              "regions": [
                "nyc1"
              ],
              "created_at": "2014-09-05T02:02:07Z"
            },
            "size": {
              "slug": "512mb",
              "transfer": 1,
              "price_monthly": 5.0,
              "price_hourly": 0.00744
            },
            "locked": false,
            "status": "new",
            "networks": {
            },
            "kernel": {
              "id": 485432972,
              "name": "Ubuntu 14.04 x64 vmlinuz-3.13.0-24-generic (1221)",
              "version": "3.13.0-24-generic"
            },
            "created_at": "2014-09-05T02:02:07Z",
            "features": [
              "virtio"
            ],
            "backup_ids": [

            ],
            "snapshot_ids": [

            ]
          },
          "links": {
            "actions": [
              {
                "id": 20,
                "rel": "create",
                "href": "http://example.org/v2/actions/20"
              }
            ]
          }
        }'''

        post.return_value = response

        client = ClientV2(token='token')
        data = client.droplets.create(name='My-Droplet', region='nyc1',
                                      size='512mb', image=449676389)

        post.assert_called_with(
            'https://api.digitalocean.com/v2/droplets',
            headers={'content-type': 'application/json',
                     'Authorization': 'Bearer token'},
            params={'name': 'My-Droplet', 'region': 'nyc1',
                    'size': '512mb', 'image': 449676389})

        assert len(data) == 2
        assert data['droplet']['id'] == 25
        assert data['droplet']['name'] == 'My-Droplet'
        assert data['droplet']['memory'] == 512
        assert data['droplet']['region']['slug'] == 'nyc1'
        assert data['links']['actions'][0]['id'] == 20
        assert data['links']['actions'][0]['rel'] == 'create'

    @mock.patch.object(requests, 'get')
    def test_get(self, get):
        response = requests.Response()
        response._content = b'''{
          "droplet": {
            "id": 20,
            "name": "test.example.com",
            "memory": 512,
            "vcpus": 1,
            "disk": 20,
            "region": {
              "slug": "nyc1",
              "name": "New York",
              "sizes": [
                "1gb",
                "512mb"
              ],
              "available": true,
              "features": [
                "virtio",
                "private_networking",
                "backups",
                "ipv6"
              ]
            },
            "image": {
              "id": 119192817,
              "name": "Ubuntu 13.04",
              "distribution": "ubuntu",
              "slug": "ubuntu1304",
              "public": true,
              "regions": [
                "nyc1"
              ],
              "created_at": "2014-09-05T02:02:05Z"
            },
            "size": {
              "slug": "512mb",
              "transfer": 1,
              "price_monthly": 5.0,
              "price_hourly": 0.00744
            },
            "locked": false,
            "status": "active",
            "networks": {
              "v4": [
                {
                  "ip_address": "127.0.0.20",
                  "netmask": "255.255.255.0",
                  "gateway": "127.0.0.21",
                  "type": "public"
                }
              ],
              "v6": [
                {
                  "ip_address": "2001::14",
                  "cidr": 124,
                  "gateway": "2400:6180:0000:00D0:0000:0000:0009:7000",
                  "type": "public"
                }
              ]
            },
            "kernel": {
              "id": 485432986,
              "name": "DO-recovery-static-fsck",
              "version": "3.8.0-25-generic"
            },
            "created_at": "2014-09-05T02:02:05Z",
            "features": [
              "ipv6"
            ],
            "backup_ids": [

            ],
            "snapshot_ids": [

            ]
          }
        }'''

        get.return_value = response

        client = ClientV2(token='token')
        data = client.droplets.get(droplet_id=20)

        get.assert_called_with(
            'https://api.digitalocean.com/v2/droplets/20',
            headers={'Authorization': 'Bearer token'},
            params={})

        assert len(data) == 1
        assert data['droplet']['id'] == 20
        assert data['droplet']['name'] == 'test.example.com'

    @mock.patch.object(requests, 'delete')
    def test_delete(self, delete):
        response = requests.Response()
        response._content = b''
        response.status_code = 204

        delete.return_value = response

        client = ClientV2(token='token')
        data = client.droplets.delete(droplet_id=123)

        delete.assert_called_with(
            'https://api.digitalocean.com/v2/droplets/123',
            headers={'content-type': 'application/x-www-form-urlencoded',
                     'Authorization': 'Bearer token'},
            params={})

        assert data == ''

    @mock.patch.object(requests, 'post')
    def test_reboot(self, post):
        response = requests.Response()
        response._content = b'''{
          "action": {
            "id": 4,
            "status": "in-progress",
            "type": "reboot",
            "started_at": "2014-09-05T02:02:01Z",
            "completed_at": null,
            "resource_id": 123,
            "resource_type": "droplet",
            "region": "nyc1"
          }
        }'''

        post.return_value = response

        client = ClientV2(token='token')
        data = client.droplets.reboot(droplet_id=123)

        post.assert_called_with(
            'https://api.digitalocean.com/v2/droplets/123/actions',
            headers={'content-type': 'application/json',
                     'Authorization': 'Bearer token'},
            params={'type': 'reboot'})

        assert len(data) == 1
        assert data['action']['id'] == 4
        assert data['action']['type'] == 'reboot'
        assert data['action']['resource_id'] == 123
        assert data['action']['resource_type'] == 'droplet'

    @mock.patch.object(requests, 'post')
    def test_power_cycle(self, post):
        response = requests.Response()
        response._content = b'''{
          "action": {
            "id": 4,
            "status": "in-progress",
            "type": "power_cycle",
            "started_at": "2014-09-05T02:02:01Z",
            "completed_at": null,
            "resource_id": 123,
            "resource_type": "droplet",
            "region": "nyc1"
          }
        }'''

        post.return_value = response

        client = ClientV2(token='token')
        data = client.droplets.power_cycle(droplet_id=123)

        post.assert_called_with(
            'https://api.digitalocean.com/v2/droplets/123/actions',
            headers={'content-type': 'application/json',
                     'Authorization': 'Bearer token'},
            params={'type': 'power_cycle'})

        assert len(data) == 1
        assert data['action']['id'] == 4
        assert data['action']['type'] == 'power_cycle'
        assert data['action']['resource_id'] == 123
        assert data['action']['resource_type'] == 'droplet'

    @mock.patch.object(requests, 'post')
    def test_shutdown(self, post):
        response = requests.Response()
        response._content = b'''{
          "action": {
            "id": 4,
            "status": "in-progress",
            "type": "shutdown",
            "started_at": "2014-09-05T02:02:01Z",
            "completed_at": null,
            "resource_id": 123,
            "resource_type": "droplet",
            "region": "nyc1"
          }
        }'''

        post.return_value = response

        client = ClientV2(token='token')
        data = client.droplets.shutdown(droplet_id=123)

        post.assert_called_with(
            'https://api.digitalocean.com/v2/droplets/123/actions',
            headers={'content-type': 'application/json',
                     'Authorization': 'Bearer token'},
            params={'type': 'shutdown'})

        assert len(data) == 1
        assert data['action']['id'] == 4
        assert data['action']['type'] == 'shutdown'
        assert data['action']['resource_id'] == 123
        assert data['action']['resource_type'] == 'droplet'

    @mock.patch.object(requests, 'post')
    def test_power_off(self, post):
        response = requests.Response()
        response._content = b'''{
          "action": {
            "id": 4,
            "status": "in-progress",
            "type": "power_off",
            "started_at": "2014-09-05T02:02:01Z",
            "completed_at": null,
            "resource_id": 123,
            "resource_type": "droplet",
            "region": "nyc1"
          }
        }'''

        post.return_value = response

        client = ClientV2(token='token')
        data = client.droplets.power_off(droplet_id=123)

        post.assert_called_with(
            'https://api.digitalocean.com/v2/droplets/123/actions',
            headers={'content-type': 'application/json',
                     'Authorization': 'Bearer token'},
            params={'type': 'power_off'})

        assert len(data) == 1
        assert data['action']['id'] == 4
        assert data['action']['type'] == 'power_off'
        assert data['action']['resource_id'] == 123
        assert data['action']['resource_type'] == 'droplet'

    @mock.patch.object(requests, 'post')
    def test_power_on(self, post):
        response = requests.Response()
        response._content = b'''{
          "action": {
            "id": 4,
            "status": "in-progress",
            "type": "power_on",
            "started_at": "2014-09-05T02:02:01Z",
            "completed_at": null,
            "resource_id": 123,
            "resource_type": "droplet",
            "region": "nyc1"
          }
        }'''

        post.return_value = response

        client = ClientV2(token='token')
        data = client.droplets.power_on(droplet_id=123)

        post.assert_called_with(
            'https://api.digitalocean.com/v2/droplets/123/actions',
            headers={'content-type': 'application/json',
                     'Authorization': 'Bearer token'},
            params={'type': 'power_on'})

        assert len(data) == 1
        assert data['action']['id'] == 4
        assert data['action']['type'] == 'power_on'
        assert data['action']['resource_id'] == 123
        assert data['action']['resource_type'] == 'droplet'

    @mock.patch.object(requests, 'post')
    def test_password_reset(self, post):
        response = requests.Response()
        response._content = b'''{
          "action": {
            "id": 4,
            "status": "in-progress",
            "type": "password_reset",
            "started_at": "2014-09-05T02:02:01Z",
            "completed_at": null,
            "resource_id": 123,
            "resource_type": "droplet",
            "region": "nyc1"
          }
        }'''

        post.return_value = response

        client = ClientV2(token='token')
        data = client.droplets.password_reset(droplet_id=123)

        post.assert_called_with(
            'https://api.digitalocean.com/v2/droplets/123/actions',
            headers={'content-type': 'application/json',
                     'Authorization': 'Bearer token'},
            params={'type': 'password_reset'})

        assert len(data) == 1
        assert data['action']['id'] == 4
        assert data['action']['type'] == 'password_reset'
        assert data['action']['resource_id'] == 123
        assert data['action']['resource_type'] == 'droplet'

    @mock.patch.object(requests, 'post')
    def test_resize(self, post):
        response = requests.Response()
        response._content = b'''{
          "action": {
            "id": 4,
            "status": "in-progress",
            "type": "resize",
            "started_at": "2014-09-05T02:02:01Z",
            "completed_at": null,
            "resource_id": 123,
            "resource_type": "droplet",
            "region": "nyc1"
          }
        }'''

        post.return_value = response

        client = ClientV2(token='token')
        data = client.droplets.resize(droplet_id=123, size='1gb')

        post.assert_called_with(
            'https://api.digitalocean.com/v2/droplets/123/actions',
            headers={'content-type': 'application/json',
                     'Authorization': 'Bearer token'},
            params={'type': 'resize', 'size': '1gb'})

        assert len(data) == 1
        assert data['action']['id'] == 4
        assert data['action']['type'] == 'resize'
        assert data['action']['resource_id'] == 123
        assert data['action']['resource_type'] == 'droplet'

    @mock.patch.object(requests, 'post')
    def test_restore(self, post):
        response = requests.Response()
        response._content = b'''{
          "action": {
            "id": 4,
            "status": "in-progress",
            "type": "restore",
            "started_at": "2014-09-05T02:02:01Z",
            "completed_at": null,
            "resource_id": 123,
            "resource_type": "droplet",
            "region": "nyc1"
          }
        }'''

        post.return_value = response

        client = ClientV2(token='token')
        data = client.droplets.restore(droplet_id=123, image=449676379)

        post.assert_called_with(
            'https://api.digitalocean.com/v2/droplets/123/actions',
            headers={'content-type': 'application/json',
                     'Authorization': 'Bearer token'},
            params={'type': 'restore', 'image': 449676379})

        assert len(data) == 1
        assert data['action']['id'] == 4
        assert data['action']['type'] == 'restore'
        assert data['action']['resource_id'] == 123
        assert data['action']['resource_type'] == 'droplet'

    @mock.patch.object(requests, 'post')
    def test_rebuild(self, post):
        response = requests.Response()
        response._content = b'''{
          "action": {
            "id": 4,
            "status": "in-progress",
            "type": "rebuild",
            "started_at": "2014-09-05T02:02:01Z",
            "completed_at": null,
            "resource_id": 123,
            "resource_type": "droplet",
            "region": "nyc1"
          }
        }'''

        post.return_value = response

        client = ClientV2(token='token')
        data = client.droplets.rebuild(droplet_id=123, image=449676379)

        post.assert_called_with(
            'https://api.digitalocean.com/v2/droplets/123/actions',
            headers={'content-type': 'application/json',
                     'Authorization': 'Bearer token'},
            params={'type': 'rebuild', 'image': 449676379})

        assert len(data) == 1
        assert data['action']['id'] == 4
        assert data['action']['type'] == 'rebuild'
        assert data['action']['resource_id'] == 123
        assert data['action']['resource_type'] == 'droplet'

        data = client.droplets.rebuild(droplet_id=123, image='image_slug')

        post.assert_called_with(
            'https://api.digitalocean.com/v2/droplets/123/actions',
            headers={'content-type': 'application/json',
                     'Authorization': 'Bearer token'},
            params={'type': 'rebuild', 'image': 'image_slug'})

        assert len(data) == 1
        assert data['action']['id'] == 4
        assert data['action']['type'] == 'rebuild'
        assert data['action']['resource_id'] == 123
        assert data['action']['resource_type'] == 'droplet'

    @mock.patch.object(requests, 'post')
    def test_rename(self, post):
        response = requests.Response()
        response._content = b'''{
          "action": {
            "id": 4,
            "status": "in-progress",
            "type": "rename",
            "started_at": "2014-09-05T02:02:01Z",
            "completed_at": null,
            "resource_id": 123,
            "resource_type": "droplet",
            "region": "nyc1"
          }
        }'''

        post.return_value = response

        client = ClientV2(token='token')
        data = client.droplets.rename(droplet_id=123, name='New Name')

        post.assert_called_with(
            'https://api.digitalocean.com/v2/droplets/123/actions',
            headers={'content-type': 'application/json',
                     'Authorization': 'Bearer token'},
            params={'type': 'rename', 'name': 'New Name'})

        assert len(data) == 1
        assert data['action']['id'] == 4
        assert data['action']['type'] == 'rename'
        assert data['action']['resource_id'] == 123
        assert data['action']['resource_type'] == 'droplet'

    @mock.patch.object(requests, 'post')
    def test_change_kernel(self, post):
        response = requests.Response()
        response._content = b'''{
          "action": {
            "id": 4,
            "status": "in-progress",
            "type": "change_kernel",
            "started_at": "2014-09-05T02:02:01Z",
            "completed_at": null,
            "resource_id": 123,
            "resource_type": "droplet",
            "region": "nyc1"
          }
        }'''

        post.return_value = response

        client = ClientV2(token='token')
        data = client.droplets.change_kernel(droplet_id=123, kernel=61833229)

        post.assert_called_with(
            'https://api.digitalocean.com/v2/droplets/123/actions',
            headers={'content-type': 'application/json',
                     'Authorization': 'Bearer token'},
            params={'type': 'change_kernel', 'kernel': 61833229})

        assert len(data) == 1
        assert data['action']['id'] == 4
        assert data['action']['type'] == 'change_kernel'
        assert data['action']['resource_id'] == 123
        assert data['action']['resource_type'] == 'droplet'

    @mock.patch.object(requests, 'post')
    def test_enable_ipv6(self, post):
        response = requests.Response()
        response._content = b'''{
          "action": {
            "id": 4,
            "status": "in-progress",
            "type": "enable_ipv6",
            "started_at": "2014-09-05T02:02:01Z",
            "completed_at": null,
            "resource_id": 123,
            "resource_type": "droplet",
            "region": "nyc1"
          }
        }'''

        post.return_value = response

        client = ClientV2(token='token')
        data = client.droplets.enable_ipv6(droplet_id=123)

        post.assert_called_with(
            'https://api.digitalocean.com/v2/droplets/123/actions',
            headers={'content-type': 'application/json',
                     'Authorization': 'Bearer token'},
            params={'type': 'enable_ipv6'})

        assert len(data) == 1
        assert data['action']['id'] == 4
        assert data['action']['type'] == 'enable_ipv6'
        assert data['action']['resource_id'] == 123
        assert data['action']['resource_type'] == 'droplet'

    @mock.patch.object(requests, 'post')
    def test_disable_backups(self, post):
        response = requests.Response()
        response._content = b'''{
          "action": {
            "id": 4,
            "status": "in-progress",
            "type": "disable_backups",
            "started_at": "2014-09-05T02:02:01Z",
            "completed_at": null,
            "resource_id": 123,
            "resource_type": "droplet",
            "region": "nyc1"
          }
        }'''

        post.return_value = response

        client = ClientV2(token='token')
        data = client.droplets.disable_backups(droplet_id=123)

        post.assert_called_with(
            'https://api.digitalocean.com/v2/droplets/123/actions',
            headers={'content-type': 'application/json',
                     'Authorization': 'Bearer token'},
            params={'type': 'disable_backups'})

        assert len(data) == 1
        assert data['action']['id'] == 4
        assert data['action']['type'] == 'disable_backups'
        assert data['action']['resource_id'] == 123
        assert data['action']['resource_type'] == 'droplet'

    @mock.patch.object(requests, 'post')
    def test_enable_private_networking(self, post):
        response = requests.Response()
        response._content = b'''{
          "action": {
            "id": 4,
            "status": "in-progress",
            "type": "enable_private_networking",
            "started_at": "2014-09-05T02:02:01Z",
            "completed_at": null,
            "resource_id": 123,
            "resource_type": "droplet",
            "region": "nyc1"
          }
        }'''

        post.return_value = response

        client = ClientV2(token='token')
        data = client.droplets.enable_private_networking(droplet_id=123)

        post.assert_called_with(
            'https://api.digitalocean.com/v2/droplets/123/actions',
            headers={'content-type': 'application/json',
                     'Authorization': 'Bearer token'},
            params={'type': 'enable_private_networking'})

        assert len(data) == 1
        assert data['action']['id'] == 4
        assert data['action']['type'] == 'enable_private_networking'
        assert data['action']['resource_id'] == 123
        assert data['action']['resource_type'] == 'droplet'

    @mock.patch.object(requests, 'post')
    def test_snapshot(self, post):
        response = requests.Response()
        response._content = b'''{
          "action": {
            "id": 4,
            "status": "in-progress",
            "type": "snapshot",
            "started_at": "2014-09-05T02:02:01Z",
            "completed_at": null,
            "resource_id": 123,
            "resource_type": "droplet",
            "region": "nyc1"
          }
        }'''

        post.return_value = response

        client = ClientV2(token='token')

        data = client.droplets.snapshot(droplet_id=123)

        post.assert_called_with(
            'https://api.digitalocean.com/v2/droplets/123/actions',
            headers={'content-type': 'application/json',
                     'Authorization': 'Bearer token'},
            params={'type': 'snapshot'})

        assert len(data) == 1
        assert data['action']['id'] == 4
        assert data['action']['type'] == 'snapshot'
        assert data['action']['resource_id'] == 123
        assert data['action']['resource_type'] == 'droplet'

        data = client.droplets.snapshot(droplet_id=123, name='nginx-fresh')

        post.assert_called_with(
            'https://api.digitalocean.com/v2/droplets/123/actions',
            headers={'content-type': 'application/json',
                     'Authorization': 'Bearer token'},
            params={'type': 'snapshot', 'name': 'nginx-fresh'})

        assert len(data) == 1
        assert data['action']['id'] == 4
        assert data['action']['type'] == 'snapshot'
        assert data['action']['resource_id'] == 123
        assert data['action']['resource_type'] == 'droplet'

    @mock.patch.object(requests, 'get')
    def test_get_droplet_action(self, get):
        response = requests.Response()
        response._content = b'''{
          "action": {
            "id": 3,
            "status": "in-progress",
            "type": "create",
            "started_at": "2014-09-05T02:02:00Z",
            "completed_at": null,
            "resource_id": 3,
            "resource_type": "droplet",
            "region": "nyc1"
          }
        }'''

        get.return_value = response

        client = ClientV2(token='token')
        data = client.droplets.get_droplet_action(droplet_id=123, action_id=3)

        get.assert_called_with(
            'https://api.digitalocean.com/v2/droplets/123/actions/3',
            headers={'Authorization': 'Bearer token'},
            params={})

        assert len(data) == 1
        assert data['action']['id'] == 3
