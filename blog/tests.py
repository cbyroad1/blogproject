from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import BlogPost, Category

class CreateBlogPostTests(TestCase):

    def setUp(self):
        url = reverse('create-post')
        self.response = self.client.get(url)
        self.title = 'My Post Title'
        self.content = 'This is the test content of my test post'

    def test_create_blog_post_page_is_returned(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed('create_post.html')

    def test_can_create_new_blog_post(self):
        category = Category.objects.create(name='Test-Category')
        author = get_user_model().objects.create_user(username = 'testuser2', email = 'testuser2@email.com', password = 'testpass123')
        blogpost = BlogPost.objects.create(title = self.title, category = category, content = self.content, author = author)
        
        self.assertEqual(blogpost.title, 'My Post Title')
        self.assertEqual(blogpost.category.name, 'Test-Category')
        self.assertEqual(blogpost.content, 'This is the test content of my test post')
        self.assertEqual(blogpost.author, author)

    
class DeleteBlogPostTests(TestCase):

    def setUp(self):
        self.title = 'My Post Title'
        self.content = 'This is the test content of my test post'

        self.category = Category.objects.create(name='Test-Category')
        self.author = get_user_model().objects.create_user(username = 'testuser2', email = 'testuser2@email.com', password = 'testpass123')
        self.blogpost = BlogPost.objects.create(title = self.title, category = self.category, content = self.content, author = self.author)

        url = reverse('delete-post', kwargs={'pk': self.blogpost.id})
        self.response = self.client.get(url)

    def test_url_returns_delete_post_page(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed('delete_post.html')

    def test_delete_blog_post_successfully(self):
        blogpost = BlogPost.objects.all()[0]
        blogpost.delete()
        self.assertFalse(BlogPost.objects.all())



    
