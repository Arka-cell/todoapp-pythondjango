from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from todo.models import User
from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory
from rest_framework.authtoken.views import obtain_auth_token
from utils.custom_log import get_log
from todo.views import TaskTypesViewset

log = get_log()

factory = APIRequestFactory()

# Create your tests here.


class AccountTest(APITestCase):
    def setUp(self) -> None:
        self.data = {
            "email": "test@email.com",
            "username": "testuser",
            "password": "s0m$Password",
        }
        self.user = User.objects.create(username=self.data["username"])
        self.user.set_password(self.data["password"])
        self.user.save()
        self.token = None
        self.sign_up_data = {
            "email": "signup@email.com",
            "username": "signupuser",
            "password": "s0m$Password",
        }

    def test_sign_up(self) -> None:
        """
        BDD Scenario signup a user:
        -GIVEN a non-registered user; Aka Anonymous User
        -WHEN he registers in the sign-up endpoint
        -THEN a successful response with status code 201
        """
        self.create_url = reverse(f"signup")
        response = self.client.post(self.create_url, self.sign_up_data, format="json")
        self.assertEqual(
            response.status_code,
            201,
            msg=f"\nStatus code is {response.status_code} instead of 201.",
        )

    def test_login(self) -> None:
        # adding fixtures

        del self.data["email"]
        # force authentication
        request = factory.post("/api/login/", data=self.data)
        force_authenticate(request, user=self.user)
        response = obtain_auth_token(request)
        response.render()
        self.assertEqual(
            response.status_code,
            200,
            msg=f"\nStatus code is {response.status_code} instead of 200.",
        )


class TestTasks(APITestCase):
    def setUp(self) -> None:
        self.user_data = {
            "email": "test@email.com",
            "username": "testuser",
        }
        self.user = User.objects.create(**self.user_data)
        self.user.set_password("s0m$Password")
        self.user.save()
        self.task_type_data = {"name": "Sports"}

    def test_post_task_type(self) -> None:
        # force authentication
        request = factory.post("/api/task-types/", data=self.task_type_data)
        force_authenticate(request, user=self.user)
        view = TaskTypesViewset.as_view({"get": "list", "post": "create"})
        response = view(request)
        response.render()
        log.info(response.content)
        self.assertEqual(
            response.status_code,
            201,
            msg=f"\nStatus code is {response.status_code} instead of 200.",
        )
        self.assertEqual(
            response.data["name"],
            self.task_type_data["name"],
            msg=f"\nStatus code is {response.data} instead of {self.task_type_data}.",
        )
