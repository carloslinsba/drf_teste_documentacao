from rest_framework import serializers
from carlosflix.models import Programa

class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programa
        fields = ['titulo', 'tipo', 'data_lancamento', 'likes']