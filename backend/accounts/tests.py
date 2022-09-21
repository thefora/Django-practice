from urllib import response
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
import json

# Create your tests here.
class SignUp(TestCase):
    def test_signup(self):
        client = Client()
        data = {
            "email" : "ash@gmail.com",
            "password1" : "1q2w3e4r!",
            "password2" : "1q2w3e4r!",
            "nickname" : "IM_Ash",
            "name" : "안세현",
            "gender" : "male"
        }
        response = client.post('/account/registration', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
    