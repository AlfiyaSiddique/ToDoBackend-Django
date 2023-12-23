from rest_framework import serializers
from .models import Todo, Tag


class TodoSerializer(serializers.ModelSerializer):
    tag_names = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = ('id', 'timestamp', 'title',
                  'description', 'dueDate', 'tag_names', 'status')

    def create(self, validated_data):
        tag_names = validated_data.pop('tag', [])
        todo = Todo.objects.create(**validated_data)
        todo.tag.set(self.get_or_create_tags(tag_names))
        return todo

    def update(self, instance, validated_data):
        tag_names = validated_data.pop('tag', [])
        instance.tag.set(self.get_or_create_tags(tag_names))
        return super().update(instance, validated_data)

    def get_or_create_tags(self, tag_names):
        tags = []
        for name in tag_names:
            tag, _ = Tag.objects.get_or_create(name=name)
            tags.append(tag)
        return tags

    def get_tag_names(self, obj):
        return [tag.name for tag in obj.tag.all()]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)
