from rest_framework import serializers
from .models import Todo, Tag


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'timestamp', 'title', 'description',
                  'dueDate', 'tag', 'status')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)
