from rest_framework import generics
from .models import Scream
from .serializers import ScreamSerializer


class ScreamLIstAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = Scream.objects.all().order_by('-id')
    serializer_class = ScreamSerializer


class ScreamCreateAPIView(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = Scream.objects.all()
    serializer_class = ScreamSerializer
