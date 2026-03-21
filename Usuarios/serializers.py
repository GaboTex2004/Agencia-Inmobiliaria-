from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'id_usuario',
            'nombres',
            'apellidos',
            'email',
            'telefono',
            'username',
            'estado'
        ]
        read_only_fields = ['creado_en', 'actualizado_en']
        
    def create(self, validated_data):
        user = Usuario(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user