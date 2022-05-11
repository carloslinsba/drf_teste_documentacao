from django.test import TestCase
from carlosflix.models import Programa
from carlosflix.serializers import ProgramaSerializer

class ProgramaSerializerTestCase(TestCase):
    
    def setUp(self):
        self.programa = Programa (
            titulo = 'Finding Nobody',
            data_lancamento = '2004-05-06',
            tipo = 'F',
            likes =2340,
            dislikes = 40
            
        )

        self.serializer = ProgramaSerializer(instance = self.programa)

    def test_verifica_campos_serializados(self):
        """Test to verify serializer attr"""
        data = self.serializer.data
        self.assertEqual(set(data.keys() ), set(['titulo', 'tipo', 'data_lancamento', 'likes'] ) )
    
    def test_verify_serialized_content(self):
        """Test to verify serializer attr content"""
        data = self.serializer.data
        self.assertEqual( data['titulo'], self.programa.titulo )
        self.assertEqual( data['data_lancamento'], self.programa.data_lancamento )
        self.assertEqual( data['tipo'], self.programa.tipo )
        self.assertEqual( data['likes'], self.programa.likes )
        

