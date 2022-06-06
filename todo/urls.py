from django.urls import path
from .views import TaskTypesViewset

urlpatterns = [
    path("task-types/", TaskTypesViewset.as_view({"get": "list", "post": "create"}), name="tasktypes"),
    path("task-types/<int:pk>", TaskTypesViewset.as_view({"get": "retrieve", "patch": "update"}), name="tasktype"),
]
