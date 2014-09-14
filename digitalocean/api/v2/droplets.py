# coding: utf-8

from digitalocean.api.baseapi import BaseAPI


class Droplets(BaseAPI):

    def __make_action(self, droplet_id, action_type, **kwargs):
        "Makes an action"

        params = {'type': action_type}
        params.update(kwargs)

        return self.request(
            'droplets/{}/actions'.format(droplet_id), 'POST', params=params)

    def all(self):
        "List all Droplets"

        return self.request('droplets', 'GET')

    def list_droplet_kernels(self, droplet_id):
        "List all available Kernels for a Droplet"

        return self.request('droplets/{}/kernels'.format(droplet_id), 'GET')

    def get_droplet_snapshots(self, droplet_id):
        "Retrieve snapshots for a Droplet"

        return self.request('droplets/{}/snapshots'.format(droplet_id), 'GET')

    def get_droplet_backups(self, droplet_id):
        "Retrieve backups for a Droplet"

        return self.request('droplets/{}/backups'.format(droplet_id), 'GET')

    def get_droplet_actions(self, droplet_id):
        "Retrieve actions for a Droplet"

        return self.request('droplets/{}/actions'.format(droplet_id), 'GET')

    def create(self, name, region, size, image, ssh_keys=None, backups=None,
               ipv6=None, private_networking=None, user_data=None):
        "Create a new Droplet"

        params = {'name': name, 'region': region, 'size': size, 'image': image}
        if ssh_keys:
            params.update({'ssh_keys': ssh_keys})
        if backups:
            params.update({'backups': backups})
        if ipv6:
            params.update({'ipv6': ipv6})
        if private_networking:
            params.update({'private_networking': private_networking})
        if user_data:
            params.update({'user_data': user_data})
        return self.request('droplets', 'POST', params=params)

    def get(self, droplet_id):
        "Retrieve an existing Droplet by id"

        return self.request('droplets/{}'.format(droplet_id), 'GET')

    def delete(self, droplet_id):
        "Delete a Droplet"

        return self.request('droplets/{}'.format(droplet_id), 'DELETE')

    def reboot(self, droplet_id):
        "Reboot a Droplet"

        return self.__make_action(droplet_id, 'reboot')

    def power_cycle(self, droplet_id):
        "Power Cycle a Droplet"

        return self.__make_action(droplet_id, 'power_cycle')

    def shutdown(self, droplet_id):
        "Shutdown a Droplet"

        return self.__make_action(droplet_id, 'shutdown')

    def power_off(self, droplet_id):
        "Power Off a Droplet"

        return self.__make_action(droplet_id, 'power_off')

    def power_on(self, droplet_id):
        "Power On a Droplet"

        return self.__make_action(droplet_id, 'power_on')

    def password_reset(self, droplet_id):
        "Password Reset a Droplet"

        return self.__make_action(droplet_id, 'password_reset')

    def resize(self, droplet_id, size):
        "Resize a Droplet"

        return self.__make_action(droplet_id, 'resize', size=size)

    def restore(self, droplet_id, image):
        "Restore a Droplet"

        return self.__make_action(droplet_id, 'restore', image=image)

    def rebuild(self, droplet_id, image):
        "Rebuild a Droplet"

        return self.__make_action(droplet_id, 'rebuild', image=image)

    def rename(self, droplet_id, name):
        "Rename a Droplet"

        return self.__make_action(droplet_id, 'rename', name=name)

    def change_kernel(self, droplet_id, kernel):
        "Change the Kernel"

        return self.__make_action(droplet_id, 'change_kernel', kernel=kernel)

    def enable_ipv6(self, droplet_id):
        "Enable IPv6"

        return self.__make_action(droplet_id, 'enable_ipv6')

    def disable_backups(self, droplet_id):
        "Disable Backups"

        return self.__make_action(droplet_id, 'disable_backups')

    def enable_private_networking(self, droplet_id):
        "Enable Private Networking"

        return self.__make_action(droplet_id, 'enable_private_networking')

    def snapshot(self, droplet_id, name=None):
        "Snapshot"

        params = {}
        if name:
            params.update({'name': name})

        return self.__make_action(droplet_id, 'snapshot', **params)

    def get_droplet_action(self, droplet_id, action_id):
        "Retrieve a Droplet Action"

        return self.request(
            'droplets/{}/actions/{}'.format(droplet_id, action_id), 'GET')
