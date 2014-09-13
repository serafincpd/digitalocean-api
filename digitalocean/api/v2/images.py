# coding: utf-8

from digitalocean.api.baseapi import BaseAPI


class Images(BaseAPI):

    def all(self):
        "List all Images"

        return self.request('images', 'GET')

    def get(self, image_id):
        "Retrieve an existing Image by id or slug"

        return self.request('images/{}'.format(image_id), 'GET')

    def delete(self, image_id):
        "Delete an Image"

        return self.request('images/{}'.format(image_id), 'DELETE')

    def update(self, image_id, name):
        "Update an Image"

        params = {'name': name}
        return self.request('images/{}'.format(image_id), 'PUT', params=params)

    def transfer(self, image_id, region):
        "Transfer an Image"

        params = {'region': region}
        return self.request(
            'images/{}/actions'.format(image_id), 'POST', params=params)

    def get_image_action(self, image_id, action_id):
        "Retrieve an existing Image Action"

        return self.request(
            'images/{}/actions/{}'.format(image_id, action_id), 'GET')
