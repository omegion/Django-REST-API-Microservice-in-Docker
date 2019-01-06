from rest_framework import generics

from deployer.models import Deployer
from api.serializers import *
from deployer.tasks import test_task

class ListDeployer(generics.ListCreateAPIView):
    queryset = Deployer.objects.all()
    serializer_class = DeployerSerializer


class DetailDeployer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deployer.objects.all()
    serializer_class = DeployerSerializer

    def get(self, request, *args, **kwargs):
        test_task.apply_async(args=["asd"], countdown=1, expires=120)
        # test_task.delay("receive get")
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        test_task("receive put")
        return self.retrieve(request, *args, **kwargs)

