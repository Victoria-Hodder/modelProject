from django.test import TestCase
from .models import Simple

class TestSimple(TestCase):

    def create_something_simple(self, text="my text", number=1, url="www.google.com"):
        return Simple.objects.create(text=text, number=number, url=url)


    def test_simple_creation(self):
        simple = self.create_something_simple()
        self.assertTrue(isinstance(simple, Simple))
        self.assertEqual(simple.__unicode__(), simple.text)