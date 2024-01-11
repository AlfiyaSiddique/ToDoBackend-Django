from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from todo.models import Todo, Tag


class AuthMixin:
    def setUp(self):
        self.user = User.objects.create_user(
            username="Alfiya", password="Alfiya@1708", is_staff=True
        )
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(self.user)


class CreateTodoViewTest(AuthMixin, TestCase):   # Test for Todo View - Create
    def test_create_todo(self):
        initial_todo_count = Todo.objects.count()
        data = {
            "title": "New Todo",
            "description": "Testing create functionality",
            "tag_names": ["Academic", "Learning"],
            "dueDate": "2024-01-29",
            "status": "Open"
        }
        response = self.client.post(reverse("createTodo"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(), initial_todo_count + 1)
        self.assertEqual(response.data.get("title"), "New Todo")


class TodoViewsTest(AuthMixin, TestCase):   # Test for Todo View - Read
    def test_todo_views(self):
        response = self.client.get(reverse("allTodo"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateTodoViewTest(AuthMixin, TestCase):  # Test for Todo View - Update
    def setUp(self):
        super().setUp()
        self.todo = Todo.objects.create(
            title="Update Me Todo", description="Testing update functionality"
        )

    def test_update_todo(self):
        data = {
            "title": "Updated Todo",
            "description": "Updated description",
            "tag_names": ["UpdatedTestTag"],
        }
        url = reverse("updateTodo", kwargs={"pk": self.todo.id})
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, "Updated Todo")


class DeleteTodoViewTest(AuthMixin, TestCase):  # Test for Todo View - Deletion
    def setUp(self):
        super().setUp()
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


class CreateTagViewTest(AuthMixin, TestCase):  # Test for Tag View - Create
    def test_create_tag(self):
        initial_tag_count = Tag.objects.count()
        data = {"name": "TestTag"}
        response = self.client.post(reverse("createTag"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tag.objects.count(), initial_tag_count + 1)
        self.assertEqual(response.data.get("name"), "TestTag")


class TagViewTest(AuthMixin, TestCase):   # Test for Tag View - Read
    def test_tag_view(self):
        response = self.client.get(reverse("allTag"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateTagViewTest(AuthMixin, TestCase):   # Test for Tag View - Update
    def setUp(self):
        super().setUp()
        self.tag = Tag.objects.create(name="UpdateMeTag")

    def test_update_tag(self):
        data = {"name": "UpdatedTag"}
        url = reverse("updateTag", kwargs={"pk": self.tag.id})
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.tag.refresh_from_db()
        self.assertEqual(self.tag.name, "UpdatedTag")


class DeleteTagViewTest(AuthMixin, TestCase):  # Test for Tag View - Deletion
    def setUp(self):
        super().setUp()
        self.tag = Tag.objects.create(name="deleteTag")

    def test_delete_todo(self):
        initial_todo_count = Tag.objects.count()
        self.url = reverse("deleteTag", kwargs={"pk": self.tag.id})
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), initial_todo_count - 1)
        self.assertEqual(response.data, {"message": "Tag deleted successfully"})
