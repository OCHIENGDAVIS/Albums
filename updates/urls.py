
from django.urls import path
from .views import UpdateModeDetaillAPIView, UpdateModeListAPIView, about

app_name = 'updates'
urlpatterns = [
    path('<int:id>/', UpdateModeDetaillAPIView.as_view()),
    path('', UpdateModeListAPIView.as_view()),
    path('about/', about, name='about'),
]