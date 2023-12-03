from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from .models import *

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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Object deleted successfully'}, status=200)


class CreateTag(generics.CreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class TagView(generics.ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class UpdateTag(generics.RetrieveUpdateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class DeleteTag(generics.DestroyAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Tag deleted successfully'}, status=200)
