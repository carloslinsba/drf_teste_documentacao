from django.test import TestCase
from carlosflix.models import Programa

class FixtureDataTestCase (TestCase):
    fixtures = ['programas_iniciais']
    