from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('programas-list')
        self.user = User.objects.create_user('c3po', password = '123456')

    def test_user_auth_correct_credentials(self):
        """Verifies if a user with correct credentials is authenticated """
        user = authenticate (username = 'c3po', password = '123456')
        self.assertTrue ((user is not None ) and user.is_authenticated)
    
    def test_user_auth_incorrect_credentials_username(self):
        """Verifies if a user with incorrect credentials -username - is not authenticated """
        user = authenticate (username = 'c3pp', password = '123456')
        self.assertFalse ((user is not None ) and user.is_authenticated)
    
    def test_user_auth_incorrect_credentials_password(self):
        """Verifies if a user with incorrect credentials - password - is not authenticated """
        user = authenticate (username = 'c3po', password = '123455')
        self.assertFalse ((user is not None ) and user.is_authenticated)
    
    def test_get_unauthorized(self):
        """Verifies if a non authenticated get gets unauhorized"""
        response = self.client.get(self.list_url)
        self.assertEqual( response.status_code, status.HTTP_401_UNAUTHORIZED)