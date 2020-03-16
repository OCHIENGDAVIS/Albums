from django.urls import path
from .views import UserProfileFeedCreate, UserProfileFeedListAPIView

urlpatterns = [
    path('feeds/', UserProfileFeedListAPIView.as_view()),
    path('feeds/create/', UserProfileFeedCreate.as_view() )
]