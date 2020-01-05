from django.urls import path
from .views import (
    StatusListAPIView,
    StatusCreateAPIView,
    StatusDeleteAPIView,
    StatusDetailAPIView,
    StatusUpdateAPIView
)


urlpatterns = [
    path('', StatusListAPIView.as_view()),
    path('create/', StatusCreateAPIView.as_view()),
    path('<int:id>/update/', StatusUpdateAPIView.as_view()),
    path('<int:id>/delete/', StatusDeleteAPIView.as_view()),
    path('<int:id>/', StatusDetailAPIView.as_view()),
]