from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.models import Group

from .forms import UserCreationForm

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

class SignUpPageTests(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)
        self.username = 'testuser123'
        self.email = 'testuser123@email.com'
        self.group = 'General'
        

    def test_signup_page_is_returned(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'accounts/signup.html')

    def test_signup_new_user(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        new_group = Group.objects.create(name=self.group)
        new_user.groups.add(new_group)

        self.assertEqual(get_user_model().objects.all()[0].groups.all()[0].name, self.group)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)


class LoginPageTests(TestCase):

    def setUp(self):
        url = reverse('login')
        self.response = self.client.get(url)
        
    def test_login_template_is_returned(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'accounts/login.html')
    
    # since django hashes the password, need to use set_password to validate with testing login()
    def test_login_user(self):
        user = get_user_model().objects.create_user(username='testuser123')
        user.set_password('testpass123')
        user.save()
        self.assertTrue(Client().login(username = 'testuser123', password = 'testpass123'))

    

    
