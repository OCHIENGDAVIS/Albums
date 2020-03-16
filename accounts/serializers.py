from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import UserProfile


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER



User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={"input_type": "password"})
    password2 = serializers.CharField(write_only=True, style={"input_type": "password"})
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'token']
        extra_kwargs = {'password': {'write_only': True}, 'password2': {'read_only_field': True}}

    def get_token(self, obj):
        user = obj
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError('passwords must match')
        return attrs

    def create(self, validated_data):
        user = User(username=validated_data.get('username'), email=validated_data.get('email'))
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class UserDisplaySerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'uri'
        ]

    def get_uri(self, obj):
        return '/api/users/{id}/'.format(id=obj.id)


class UserDetailSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'uri',
    
        ]

    def get_uri(self, obj):
        return '/api/users/{id}/'.format(id=obj.id)


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our API"""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """A User profile object serializer"""

    class Meta:
        model = UserProfile
        fields = ['id', 'email', 'name', 'password']
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):
        """Create and return  a new user"""
        user = UserProfile(
            email=validated_data.get('email'),
            name=validated_data.get('name')
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user









