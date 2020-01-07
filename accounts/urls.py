
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from .views import AuthRegister, RegisterAPIView, UserDetailAPIView


urlpatterns = [
    path('token/', obtain_jwt_token),
    path('token/refresh/', refresh_jwt_token),
    path('token/verify/', verify_jwt_token),
    path('register/', RegisterAPIView.as_view()),
    path('users/<str:username>/', UserDetailAPIView.as_view()),
]
