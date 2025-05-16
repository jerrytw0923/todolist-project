from django.urls import path
from .views import todolist, viewtodo, createtodo

urlpatterns = [
    path("", todolist, name="todolist"),
    path("view/<int:id>/", viewtodo, name="viewtodo"),
    path("create/", createtodo, name="createtodo"),
]
