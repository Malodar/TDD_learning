from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from .views import home_page

# Create your tests here.


class SmokeTest(TestCase):
    """тест домашней страницы"""

    def test_root_url_resolvers_to_home_page_view(self):
        """тест: корневой URL преобразуется в представление домашней страницы"""
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        """test: home page return correct html"""
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
