from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import ProfileFeedItemSerializer
from .models import ProfileFeedItem
from .permissions import PostOwnStatus


class UserProfileFeedListAPIView(generics.ListAPIView):
    serializer_class = ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()
    permission_classes = (IsAuthenticated, )


class UserProfileFeedCreate(generics.CreateAPIView):
    serializer_class = ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()
    permission_classes = (PostOwnStatus, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        print('performing some create!!')
        if not self.request.user.is_authenticated:
            return Response({'message': 'You are not authenticated, please login first'})
        return serializer.save(user_profile=self.request.user)


