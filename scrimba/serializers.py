from rest_framework.serializers import ModelSerializer
from .models import Scream


class ScreamSerializer(ModelSerializer):

    class Meta:
        model = Scream
        fields = ['id', 'userHandle', 'body', 'createdAt']
