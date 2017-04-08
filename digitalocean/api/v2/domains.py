# coding: utf-8

from digitalocean.api.baseapi import BaseAPI


class Domains(BaseAPI):

    def all(self):
        "List all Domains"

        return self.request('domains', 'GET')

    def create(self, name, ip_address):
        "Create a new Domain"

        params = {'name': name, 'ip_address': ip_address}
        return self.request('domains', 'POST', params=params)

    def get(self, domain_id):
        "Retrieve an existing Domain"

        return self.request('domains/{}'.format(domain_id), 'GET')

    def delete(self, domain_id):
        "Delete a Domain"

        return self.request('domains/{}'.format(domain_id), 'DELETE')

    def list_domain_records(self, domain_id):
        "List all Domain Records"

        return self.request('domains/{}/records'.format(domain_id), 'GET')

    def create_domain_record(self, domain_id, rtype=None, name=None, data=None,
                             priority=None, port=None, weight=None):
        "Create a new Domain Record"

        params = {'type': rtype}
        if name:
            params.update({'name': name})
        if data:
            params.update({'data': data})
        if priority:
            params.update({'priority': priority})
        if port:
            params.update({'port': port})
        if weight:
            params.update({'weight': weight})
        return self.request(
            'domains/{}/records'.format(domain_id), 'POST', params=params)

    def get_domain_record(self, domain_id, record_id):
        "Retrieve an existing Domain Record"

        return self.request(
            'domains/{}/records/{}'.format(domain_id, record_id), 'GET')

    def delete_domain_record(self, domain_id, record_id):
        "Delete a Domain Record"

        return self.request(
            'domains/{}/records/{}'.format(domain_id, record_id), 'DELETE')

    def update_domain_record(self, domain_id, record_id, name=None, data=None):
        "Update a Domain Record"

        params = {}

        if name:
            params.update({'name': name})
        if data:
            params.update({'data': data})

        return self.request('domains/{}/records/{}'.format(
            domain_id, record_id), 'PUT', params=params)
