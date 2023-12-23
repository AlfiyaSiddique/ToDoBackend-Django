from django.urls import path
from todo import views

urlpatterns = [
    path("todo/<int:pk>/", views.UpdateTodo.as_view(), name="updateTodo"),
    path("todo", views.TodoViews.as_view(), name="allTodo"),
    path("create", views.CreateTodo.as_view(), name="createTodo"),
    path("delete/<int:pk>", views.DeleteTodo.as_view(), name="deleteTodo"),
    path("create/tag", views.CreateTag.as_view(), name="createTag"),
    path("tag", views.TagView.as_view(), name="allTag"),
    path("tag/<int:pk>/", views.UpdateTag.as_view(), name="updateTag"),
    path("delete/tag/<int:pk>", views.DeleteTag.as_view(), name="deleteTag"),
]
