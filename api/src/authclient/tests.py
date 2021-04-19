from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from customuser.models import Client


class RegistrationClientTests(APITestCase):

    def setUp(self):
        self.user = Client.objects.create_client(
            username='test',
            email='test@gmail.com',
            password='2869804p')

        self.client = APIClient()

    def test_create_client(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('register')
        data = {
            'username': 'poproshu',
            'email': 'poproshu@gmail.com',
            'password': '2869804p',
            'password2': '2869804p'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.last().username, 'poproshu')
        self.assertEqual(Client.objects.last().email, 'poproshu@gmail.com')
    
    def test_password_mismathing(self):
        """
        Ensure we have password==password2.
        """
        url = reverse('register')
        data = {
            'username': 'poproshu',
            'email': 'poproshu@gmail.com',
            'password': '2869804p',
            'password2': '2869804'}
        response = self.client.post(url, data, format='json')
        self.assertIn('passwordError', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_password_is_digit(self):
        """
        Ensure we have password that has not only digits.
        """
        url = reverse('register')
        data = {
            'username': 'poproshu',
            'email': 'poproshu@gmail.com',
            'password': '28698040',
            'password2': '28698040'}
        response = self.client.post(url, data, format='json')
        self.assertIn('password', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_password_is_less_then_8_symbols(self):
        """
        Ensure we have password lenght more than 8 symbols.
        """
        url = reverse('register')
        data = {
            'username': 'poproshu',
            'email': 'poproshu@gmail.com',
            'password': '286980p',
            'password2': '286980p'}
        response = self.client.post(url, data, format='json')
        self.assertIn('password', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_email_exists(self):
        """
        Ensure we can get token.
        """
        url = reverse('register')
        data = {
            'username': 'poproshu',
            'email': 'test@gmail.com',
            'password': '2869804p',
            'password2': '2869804p'}
        response = self.client.post(url, data, format='json')
        self.assertIn('email', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_username_exists(self):
        """
        Ensure we can get token.
        """
        url = reverse('register')
        data = {
            'username': 'test',
            'email': 'testa@gmail.com',
            'password': '2869804p',
            'password2': '2869804p'}
        response = self.client.post(url, data, format='json')
        self.assertIn('username', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    

class AuthClientTests(APITestCase):

    def setUp(self):
        self.user = Client.objects.create_client(
            username='test',
            email='test@gmail.com',
            password='2869804p')

        self.client = APIClient()

    def test_get_token_with_email(self):
        """
        Ensure we can get token with email
        """
        url = reverse('login')
        data = {
            'email_or_username':'test@gmail.com',
            'password':'2869804p'
            }
        response = self.client.post(url, data, format='json')
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_token_with_username(self):
        """
        Ensure we can get token with username
        """
        url = reverse('login')
        data = {
            'email_or_username':'test',
            'password':'2869804p'
            }
        response = self.client.post(url, data, format='json')
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_if_wrong_email_or_username_field(self):
        """
        Ensure we can get Error with wrong email_or_username field
        """
        url = reverse('login')
        data = {
            'email_or_username':'testt',
            'password':'2869804p'
            }
        response = self.client.post(url, data, format='json')
        self.assertIn('LoginError', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_if_wrong_password(self):
        """
        Ensure we can Error with wrong password
        """
        url = reverse('login')
        data = {
            'email_or_username':'test',
            'password':'2869804'
            }
        response = self.client.post(url, data, format='json')
        self.assertIn('LoginError', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)