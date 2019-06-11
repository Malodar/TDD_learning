from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from .views import home_page

# Create your tests here.


class SmokeTest(TestCase):
    """тест домашней страницы"""

    def test_uses_home_template(self):
        """test: home page return correct html"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')

    def test_can_save_a_post_request(self):
        """test: can save POST request"""
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'lists/home.html')
