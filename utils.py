from django.conf import settings
from django.utils import timezone
from rest_framework_jwt.settings import api_settings


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': user.name,
        'expires' : timezone.now() + api_settings.JWT_REFRESH_EXPIRATION_DELTA - timezone.timedelta(seconds=200),
    }