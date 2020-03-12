from rest_framework import generics
from .models import Expense, Todo
from . import serializers


class ExpenseListApiView(generics.ListAPIView):
    queryset = Expense.objects.all()
    permission_classes = []
    authentication_classes = []
    serializer_class = serializers.ExpenseSerializer


class ExpenseDetailAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    authentication_classes = []
    permission_classes = []
    queryset = Expense.objects.all()
    serializer_class = serializers.ExpenseSerializer


class ExpenseCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.ExpenseSerializer
    authentication_classes = []
    permission_classes = []
    queryset = Expense.objects.all()


class ExpenseDeleteAPIView(generics.DestroyAPIView):
    lookup_field = 'id'
    permission_classes = []
    authentication_classes = []
    queryset = Expense.objects.all()
    serializer_class = serializers.ExpenseSerializer


class ExpenseUpdateAPIView(generics.UpdateAPIView):
    lookup_field = 'id'
    serializer_class = serializers.ExpenseSerializer
    permission_classes = []
    authentication_classes = []

# The ToDO App API views


class ToDoListAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = serializers.TodoSerializer
    queryset = Todo.objects.all()


class ToDoDetailAPIView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = serializers.TodoSerializer
    queryset = Todo.objects.all()
    lookup_field = 'id'


class ToDoUpdateAPIView(generics.UpdateAPIView):
    authentication_classes = []
    permission_classes = []
    lookup_field = 'id'
    serializer_class = serializers.TodoSerializer
    queryset = Todo.objects.all()


class TodoDeleteAPIView(generics.DestroyAPIView):
    authentication_classes = []
    permission_classes = []
    lookup_field = 'id'
    serializer_class = serializers.TodoSerializer
    queryset = Todo.objects.all()


class TodoCreateAPIView(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = serializers.TodoSerializer






