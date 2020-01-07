from rest_framework import serializers
from .models import Status
from accounts.serializers import UserDisplaySerializer


class StatusSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)

    class Meta:
        model = Status
        fields = ['id','user', 'content', 'image']




