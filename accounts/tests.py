from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class RegistrationTest(TestCase):
    def test_registration_page_loads(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Register')

    def test_user_registration(self):
        User = get_user_model()
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'Testpass123!',
            'password2': 'Testpass123!',
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(User.objects.filter(username='testuser').count(), 1)

class LoginTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='loginuser', email='login@example.com', password='Testpass123!', is_active=True)

    def test_login_page_loads(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Login')

    def test_user_login(self):
        login = self.client.login(username='loginuser', password='Testpass123!')
        self.assertTrue(login)
