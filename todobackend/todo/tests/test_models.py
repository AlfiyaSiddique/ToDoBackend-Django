from django.test import TestCase
from todo.models import *
from django.utils import timezone


# models test


class TestTag(TestCase):

    def create_tag(self, name="TestTag1"):
        return Tag.objects.create(name=name)

    def test_Tag_creation(self):
        w = self.create_tag()
        self.assertTrue(isinstance(w, Tag))
        self.assertEqual(str(w), w.name)


class TestTodo(TestCase):

    def create_todo(self, title="Add a test for application", description="Test Application",
                    due_date="2023-12-06", tag="Learning", status="OPEN"):
        todo = Todo.objects.create(title=title, description=description, dueDate=due_date,
                                   status=status, timestamp=timezone.now())

        try:
            tag_obj = Tag.objects.get(name=tag)
        except Tag.DoesNotExist:
            # Create the tag if it doesn't exist
            tag_obj = Tag.objects.create(name=tag)

            # Associate the tag with the Todo
        todo.tag.add(tag_obj)
        return todo

    def test_Todo_creation(self):
        w = self.create_todo()
        self.assertTrue(isinstance(w, Todo))
        self.assertEqual(str(w), w.title)
