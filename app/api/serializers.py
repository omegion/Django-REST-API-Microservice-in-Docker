from rest_framework import serializers
from deployer.models import Deployer

class DeployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deployer
        fields = (
            'id',
            'queue_id',
            'url'
        )