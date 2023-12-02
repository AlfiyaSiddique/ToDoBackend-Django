from django.shortcuts import render
from rest_framework import generics
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.


class CreateTodo(generics.CreateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

class TodoViews(generics.ListAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class UpdateTodo(generics.RetrieveUpdateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class DeleteTodo(generics.DestroyAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
