from rest_framework import serializers
from .models import Expense, Todo


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'description', 'note', 'amount', 'createdAt']


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'marked', 'createdAt', 'updated']
