# coding: utf-8

from digitalocean.api.baseapi import BaseAPI


class Domains(BaseAPI):

    def all(self):
        "List all Domains"

        return self.request('domains', 'GET')

    def create(self, name, ip_addr):
        "Create a new Domain"

        params = {'name': name, 'ip_address': ip_addr}
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

    def create_domain_record(self, domain_id, rtype, name, data,
                             priority, port, weight):
        "Create a new Domain Record"

        params = {'type': rtype, 'name': name, 'data': data,
                  'priority': priority, 'port': port, 'weight': weight}
        return self.request('domains/{}/records', 'POST', params=params)

    def get_domain_record(self, domain_id, record_id):
        "Retrieve an existing Domain Record"

        return self.request(
            'domains/{}/records/{}'.format(domain_id, record_id), 'GET')

    def delete_domain_record(self, domain_id, record_id):
        "Delete a Domain Record"

        return self.request(
            'domains/{}/records/{}'.format(domain_id, record_id), 'DELETE')

    def update_domain_record(self, domain_id, record_id, name):
        "Update a Domain Record"

        params = {'name': name}
        return self.request('domains/{}/records/{}'.format(
            domain_id, record_id), 'PUT', params=params)
