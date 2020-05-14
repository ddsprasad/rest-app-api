
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successful"""
        email = 'ddsprasad@gmail.com'
        password = 'Welcome@123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_name_normalized(self):
        """Test creating a new user with for normization"""
        email = 'ddsprasad@GMAIL.COM'
        password = 'Welcome@123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invlaid_user(self):
        """Test creating user with out email address"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Welcome@123')

    def test_create_new_super_user(self):
        """Test to creating a new super user"""
        email = 'ddunga@getdiwo.com'
        password = 'Welcome@123'

        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
