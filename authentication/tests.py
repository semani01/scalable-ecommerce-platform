from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()

class AuthenticationTests(APITestCase):
    def test_register_user(self):
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword"
        }
        response = self.client.post('/api/auth/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        data = {
            "username": "testuser",
            "password": "testpassword"
        }
        response = self.client.post('/api/auth/login/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
