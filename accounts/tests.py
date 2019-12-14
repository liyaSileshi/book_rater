from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class accountTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)

class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)
        self.assertTrue(response.context['user'].is_authenticated) 

    def test_logout(self):
        response = self.client.post('/accounts/logout/', self.credentials, follow=True)
        # should be logged in now
        self.assertFalse(response.context['user'].is_active)
        self.assertFalse(response.context['user'].is_authenticated)