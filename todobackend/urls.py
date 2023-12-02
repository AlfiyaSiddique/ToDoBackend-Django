from django.urls import path
from todo import views

urlpatterns = [
    path('todo/<int:pk>/', views.UpdateTodo.as_view()),
    path('todo', views.TodoViews.as_view()),
    path('create', views.CreateTodo.as_view()),
    path('delete/<int:pk>', views.DeleteTodo.as_view())
]