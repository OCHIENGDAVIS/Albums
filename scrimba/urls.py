from django.urls import path
from .views import (
    ScreamLIstAPIView,
    ScreamCreateAPIView
)

urlpatterns = [
    path('', ScreamLIstAPIView.as_view()),
    path('create/', ScreamCreateAPIView.as_view()),
]
