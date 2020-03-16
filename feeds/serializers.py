from rest_framework import serializers
from .models import ProfileFeedItem


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializer for the profile feed items"""
    class Meta:
        model = ProfileFeedItem
        fields = ('id', 'status_text', 'created_on', 'user_profile')
        extra_kwargs = {'user_profile': {'read_only': True}}
