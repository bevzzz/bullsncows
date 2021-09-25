# Third-party libraries
from django.test import TestCase
from django.urls import resolve
from src.client.components.start import home_page


class HomePageTest(TestCase):

    def test_bad_maths(self) -> None:
        self.assertEqual(1+1, 3)
