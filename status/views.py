from rest_framework.generics import ListAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView
from .serializers import StatusSerializer
from .models import Status
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication


class StatusListAPIView(ListAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()


class StatusCreateAPIView(CreateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StatusSerializer
    queryset = Status.objects.all()


class StatusDetailAPIView(RetrieveAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = 'id'


class StatusUpdateAPIView(UpdateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = 'id'


class StatusDeleteAPIView(DestroyAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = 'id'

