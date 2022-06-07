from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from todo.models import Task, TaskType
from django.db.models import Q
from .serializers import SignUpSerializer, TaskTypeSerializer, TaskSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.generics import CreateAPIView


# Create your views here.


class SignUpView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = SignUpSerializer

    def create(self, request, *args, **kwargs):
        """
        POST HTTP request containing email and password
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {**serializer.data},
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

    def perform_create(self, serializer):
        """
        Perform user creation
        """
        user = serializer.save()
        return user


class TaskTypesViewset(viewsets.ModelViewSet):
    serializer_class = TaskTypeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TaskType.objects.filter(Q(user=self.request.user) | Q(user=None))


class TasksViewset(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
