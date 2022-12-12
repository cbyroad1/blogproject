from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

class CustomUserTests(TestCase):

    def test_create_custom_user(self):
        User = get_user_model()
        user = User.objects.create_user(username = 'testuser2', email = 'testuser2@email.com', password = 'testpass123')

        self.assertEqual(user.username, 'testuser2')
        self.assertEqual(user.email, 'testuser2@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(username = 'adminuser1', email = 'adminuser1@email.com', password = 'testpass123')

        self.assertEqual(admin_user.username, 'adminuser1')
        self.assertEqual(admin_user.email, 'adminuser1@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


