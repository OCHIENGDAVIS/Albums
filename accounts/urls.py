
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from .views import (
    RegisterAPIView,
    UserDetailAPIView,
    HelloAPIView,
    HelloViewSets,
    UserProfileAPIView,
    UserProfileCreateAPIView,
    UserLogin,

)
# viewset import
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', HelloViewSets,basename='hello-viewset')

urlpatterns = [
    path('token/', obtain_jwt_token),
    path('token/refresh/', refresh_jwt_token),
    path('token/verify/', verify_jwt_token),
    path('register/', RegisterAPIView.as_view()),
    path('users/<str:username>/', UserDetailAPIView.as_view()),
    path('testing/hello/', HelloAPIView.as_view()),
    path('', include(router.urls)),
    path('profiles/', UserProfileAPIView.as_view()),
    path('profiles/create/', UserProfileCreateAPIView.as_view()),
    path('profiles/login/', UserLogin.as_view())
]
