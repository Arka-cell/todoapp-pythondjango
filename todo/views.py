from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from todo.models import Task, TaskType
from django.db.models import Q

# Create your views here.

class TaskTypesViewset(viewsets.ModelViewSet):
    def get_queryset(self):
        return TaskType.objects.filter(Q(user=self.request.user) | Q(user=None))
