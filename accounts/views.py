from django.contrib.auth import authenticate, get_user_model
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView, UpdateAPIView
from rest_framework import permissions
from rest_framework import status
from rest_framework import filters
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserRegisterSerializer, UserDetailSerializer, HelloSerializer, UserProfileSerializer
from .permission import AnonPermissionOnly
from rest_framework import viewsets
from .models import UserProfile

from .permission import UpdateOwnProfile

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
User = get_user_model()


class  AuthRegister(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny, AnonPermissionOnly]

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


class RegisterAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()
    authentication_classes = []
    permission_classes = [AnonPermissionOnly]

    # def get_serializer_context(self, request):
    #     return {'request': self.request}


class UserDetailAPIView(RetrieveAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = UserDetailSerializer
    queryset = User.objects.filter(is_active=True)
    lookup_field = 'username'


class HelloAPIView(APIView):
    """Test API view"""

    serializer_class = HelloSerializer

    def get(self, request, format=None):

        '''Return a list if features of the APIView'''
        an_Apiview = [
            'Uses HTTP methods as functions(get, post, delete, put, patch)',
            'It it similar to a traditional django view',
            'gives you the most cotrol over your API',
            'its mapped mannually to URLS'
        ]
        return Response({'message' : an_Apiview })

    def post(self, request):
        """Creates an hello message with our name"""
        serializer = HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HelloViewSets(viewsets.ViewSet):
    """Test api viewset"""

    def list(self, request):
        """Return an hello messsage"""
        a_viewset = [
            'uses actions (list, create, retrieve, update. partial_update, delete)'
        ]
        return Response({'message': 'Hello', 'a_viewset': a_viewset})


class UserProfileAPIView(ListAPIView):
    """Endpoint powering the the user profile endpoints"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email')


class UserProfileCreateAPIView(CreateAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class UserLogin(ObtainAuthToken):
    """Checks email and password and returns an auth token"""
    serializer_class = AuthTokenSerializer

    def get(self, request, format=None  ):
        return Response({'Message': 'Something nice'})
