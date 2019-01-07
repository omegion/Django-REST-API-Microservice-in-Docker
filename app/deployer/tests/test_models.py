from django.test import TestCase
from django.urls import reverse

from deployer.models import Deployer


class TestDeployerModel(TestCase):

    def setUp(self):
        self.deploy = Deployer(queue_id='i347477', url='https://google.com')
        self.deploy.save()

    def test_deployer_creation(self):
        self.assertEqual(Deployer.objects.count(), 1)

    def test_deployer_representation(self):
        self.assertEqual(self.deploy.queue_id, str(self.deploy))

    # def test_deployer_queue_id(self):
    #     deploy = Deployer.objects.get(id=1)
    #     expected_object_name = f'{deploy.queue_id}'
    #     self.assertEquals(expected_object_name, self.deploy.queue_id)

    # def test_deployer_url(self):
    #     deploy = Deployer.objects.get(id=1)
    #     expected_object_name = f'{deploy.url}'
    #     self.assertEquals(expected_object_name, self.deploy.url)
