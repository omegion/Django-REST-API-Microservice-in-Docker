from django.shortcuts import reverse
from django.test.client import Client
from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from deployer.models import Deployer

URL_PREFIX = f'api.v1.deploys'

class TestNoteApi(APITestCase):
    def setUp(self):
        # create a user for authentication
        self.client = Client()
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')

        # create deploy
        self.deploy = Deployer(
            queue_id="i747474", 
            url='https://google.com'
        )
        self.deploy.save()
    
    def test_deploy_creation(self):
        response = self.client.post(reverse(URL_PREFIX), {
            'queue_id': 'i747475',
            'url': 'https://google.net'
        })

        # assert new deploy was added
        self.assertEqual(Deployer.objects.count(), 2)

        # assert a created status code was returned
        self.assertEqual(201, response.status_code)

    def test_getting_deploys(self):
        response = self.client.get(reverse(URL_PREFIX), format="json")

        # assert setUp deploy is listed
        self.assertEqual(len(response.data), 1)

    def test_updating_deploy(self):
        import json

        # create new deploy fields
        new_deploy = {
            "queue_id": "i747475",
            "url": "https://google.net"
        }

        response = self.client.put(
            reverse(URL_PREFIX+'.detail', kwargs={'pk': self.deploy.id}), 
            json.dumps(new_deploy), 
            content_type='application/json'
        )

        # check info returned has the update
        self.assertEqual('asd', response.data['queue_id'])

    def test_deleting_deploy(self):
        response = self.client.delete(reverse(URL_PREFIX+'.detail', kwargs={'pk': self.deploy.id}))

        # assert the deploy is deleted successfully
        self.assertEqual(204, response.status_code)