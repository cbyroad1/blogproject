from django.test import TestCase
from django.urls import reverse, resolve
# Create your tests here.

class HomePageTests(TestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_uses_home_template(self):
        self.assertTemplateUsed(self.response, 'index.html')

    def test_home_returns_page(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, 'homepage')
