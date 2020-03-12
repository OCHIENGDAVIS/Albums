from django.urls import path
from . import views


urlpatterns = [
    path('', views.ExpenseListApiView.as_view()),
    path('create/', views.ExpenseCreateAPIView.as_view()),
    path('<int:id>/', views.ExpenseDetailAPIView.as_view()),
    path('<int:id>/delete/', views.ExpenseDeleteAPIView.as_view()),
    path('<int:id>/update/', views.ExpenseUpdateAPIView.as_view()),
    path('todo/', views.ToDoListAPIView.as_view()),
    path('todo/create/', views.TodoCreateAPIView.as_view()),
    path('todo/<int:id>/', views.ToDoDetailAPIView.as_view()),
    path('todo/<int:id>/edit/', views.ToDoUpdateAPIView.as_view()),
    path('todo/<int:id>/delete/', views.TodoDeleteAPIView.as_view()),

]