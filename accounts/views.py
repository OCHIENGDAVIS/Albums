from django.contrib.auth import authenticate, get_user_model
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
User = get_user_model()


class  AuthRegister(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({'detail': 'you are already authenticated'}, status=status.HTTP_400_BAD_REQUEST)
        username = request.data.get('username')
        password = request.data.get('password')
        user = User(username=username)
        user.set_password(password)
        user.save()
        user = authenticate(request, username=username, password=password)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response({'token': token})
