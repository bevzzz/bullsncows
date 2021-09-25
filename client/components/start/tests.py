# Third-party libraries
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

# Local libraries
from client.components.start.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # arrange
        request = HttpRequest()
        # act
        response = home_page(request)
        html = response.content.decode("utf8")
        # assert
        self.assertTrue(html.startswith("<html>"))
        self.assertIn("<title>Bulls and Cows</title>", html)
        self.assertTrue(html.endswith("</html>"))



