from rest_framework import generics
from rest_framework.response import Response
from .serializers import TodoSerializer, TagSerializer
from .models import Todo, Tag

# Create your views here.


class CreateTodo(generics.CreateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def perform_create(self, serializer):
        tag_names = self.request.data.get('tag_names', [])
        todo = serializer.save()
        tags = serializer.get_or_create_tags(tag_names)
        print(tags)
        todo.tag.set(tags)


class TodoViews(generics.ListAPIView):  # Read API for Todo Model
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class UpdateTodo(generics.RetrieveUpdateAPIView):  # Update API for Todo Model
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def perform_update(self, serializer):
        tag_names = self.request.data.get('tag_names', [])
        todo = serializer.save()
        todo.tag.set(serializer.get_or_create_tags(tag_names))


class DeleteTodo(generics.DestroyAPIView):  # Delete API for Todo Model
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Object deleted successfully'}, status=200)


class CreateTag(generics.CreateAPIView):  # Create API for Tag Model
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class TagView(generics.ListAPIView):  # Read API for Tag Model
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class UpdateTag(generics.RetrieveUpdateAPIView):  # Update API for Tag Model
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class DeleteTag(generics.DestroyAPIView):  # Delete API for Tag Model
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Tag deleted successfully'}, status=200)
