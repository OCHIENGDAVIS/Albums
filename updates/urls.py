
from django.urls import path
from .views import UpdateModeDetaillAPIView, UpdateModeListAPIView

urlpatterns = [
    path('<int:id>/', UpdateModeDetaillAPIView.as_view()),
    path('', UpdateModeListAPIView.as_view()),
]