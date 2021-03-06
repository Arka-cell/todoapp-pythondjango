from django.urls import path
from .views import TaskTypesViewset, SignUpView, TasksViewset
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken import views

urlpatterns = [
    path(
        "task-types/",
        TaskTypesViewset.as_view({"get": "list", "post": "create"}),
        name="tasktypes",
    ),
    path(
        "task-types/<int:pk>",
        TaskTypesViewset.as_view({"get": "retrieve", "patch": "partial_update"}),
        name="tasktype",
    ),
    path("tasks/", TasksViewset.as_view({"get": "list", "post": "create"})),
    path(
        "tasks/<int:pk>",
        TasksViewset.as_view({"get": "retrieve", "patch": "partial_update"}),
    ),
    path("login/", views.obtain_auth_token, name="login"),
    path("sign-up/", SignUpView.as_view(), name="signup"),
]
