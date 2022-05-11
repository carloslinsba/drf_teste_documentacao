from django.test import TestCase
from carlosflix.models import Programa

class ProgramaModelTestCase (TestCase):
    
    def setUp(self):
        self.programa = Programa(
            titulo = 'Finding Nobody',
            data_lancamento = '2004-05-06'
        )

    def test_verifica_atributos(self):
        """Test verifying program default attr"""
        self.assertEqual(self.programa.titulo, 'Finding Nobody')
        self.assertEqual(self.programa.tipo, 'F')
        self.assertEqual(self.programa.data_lancamento, '2004-05-06')
        self.assertEqual(self.programa.likes, 0)
        self.assertEqual(self.programa.dislikes, 0)