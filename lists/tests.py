from django.test import TestCase
from django.urls import resolve
from .views import home_page

# Create your tests here.


class SmokeTest(TestCase):
    """тест домашней страницы"""

    def test_root_url_resolvers_to_home_page_view(self):
        """тест: корневой URL преобразуется в представление домашней страницы"""
        found = resolve('/')
        self.assertEqual(found.func, home_page)
