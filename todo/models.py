from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TaskType(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="usertasktype",
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=50)


class Task(models.Model):
    user = models.ForeignKey(User, related_name="usertask", on_delete=models.CASCADE)
    task_type = models.ForeignKey(TaskType, related_name="tasktype", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    has_finished = models.BooleanField(default=False)
