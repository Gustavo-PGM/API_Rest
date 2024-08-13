from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer): #Nome para serializar
    class Meta:
        model = Usuario #Modelo para serializar para json
        fields ='__all__' #Quais os campos para serializar