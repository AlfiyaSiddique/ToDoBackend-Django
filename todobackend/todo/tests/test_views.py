from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from todo.models import Todo, Tag


class DeleteTodoViewTest(TestCase):  # Test for Todo View - Deletion
    def setUp(self):
        self.user = User.objects.create_user(
            username="Alfiya", password="Alfiya@1708", is_staff=True
        )
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.todo = Todo.objects.create(
            title="Test Todo", description="Testing delete functionality"
        )

    def test_delete_todo(self):
        initial_todo_count = Todo.objects.count()
        self.url = reverse("deleteTodo", kwargs={"pk": self.todo.id})
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), initial_todo_count - 1)
        self.assertEqual(response.data, {"message": "Object deleted successfully"})


class DeleteTagViewTest(TestCase):  # Test for Tag View - Deletion
    def setUp(self):
        self.user = User.objects.create_user(
            username="Alfiya", password="Alfiya@1708", is_staff=True
        )
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.tag = Tag.objects.create(name="deleteTag")

    def test_delete_todo(self):
        initial_todo_count = Tag.objects.count()
        self.url = reverse("deleteTag", kwargs={"pk": self.tag.id})
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), initial_todo_count - 1)
        self.assertEqual(response.data, {"message": "Tag deleted successfully"})
