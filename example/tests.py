from django.test import TestCase
from .models import Simple

class TestSimple(TestCase):

    def create_something_simple(self, text="my text", number=1, url="www.google.com"):
        return Simple.objects.create(text=text, number=number, url=url)
        # this does not run as a test because it does not have the naming convention "tests_" at the beginning

    def test_simple_creation(self):
        simple = self.create_something_simple()
        self.assertTrue(isinstance(simple, Simple))
        self.assertEqual(simple.__str__(), simple.text)


#resource used: https://realpython.com/testing-in-django-part-1-best-practices-and-examples/#testing-models