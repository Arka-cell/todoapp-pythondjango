from django.urls import path
from .views import TaskTypesViewset, SignUpView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path("task-types/", TaskTypesViewset.as_view({"get": "list", "post": "create"}), name="tasktypes"),
    path("task-types/<int:pk>", TaskTypesViewset.as_view({"get": "retrieve", "patch": "update"}), name="tasktype"),
    path("login/", ObtainAuthToken.as_view(), name="login"),
    path("sign-up/", SignUpView.as_view(), name="signup")
]
