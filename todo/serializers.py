from wsgiref import validate
from rest_framework import serializers
from todo.models import TaskType, User, Task
from django.contrib.auth.forms import PasswordResetForm


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = ["email", "password", "username"]
        extra_kwargs = {"email": {"required": True}, "username": {"required": True}}

    def validate_email(self, value):
        self.form = PasswordResetForm(data=self.initial_data)

        if not self.form.is_valid():
            raise serializers.ValidationError(self.form.errors)
        return value

    def send_mail(self, **kwargs):
        pass

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class TaskTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskType
        fields = ["id", "name"]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "name", "description", "has_finished"]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
