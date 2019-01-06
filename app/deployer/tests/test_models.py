from django.test import TestCase
from django.urls import reverse

from deployer.models import Deployer


class DeployerTests(TestCase):

    def setUp(self):
        Deployer.objects.create(queue_id='i347477', url='https://google.com')

    def test_text_content(self):
        deploy = Deployer.objects.get(id=1)
        expected_object_name = f'{deploy.queue_id}'
        self.assertEquals(expected_object_name, 'i347477')
