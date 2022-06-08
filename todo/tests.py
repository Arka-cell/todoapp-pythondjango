from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from todo.models import User
from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory
from rest_framework.authtoken.views import obtain_auth_token
from utils.custom_log import get_log

log = get_log()

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
    
