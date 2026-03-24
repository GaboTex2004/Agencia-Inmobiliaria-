from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = [
            'id_usuario',
            'nombres',
            'apellidos',
            'email',
            'telefono',
            'username',
            'estado',
            'password'  
        ]
        read_only_fields = ['creado_en', 'actualizado_en']

    def create(self, validated_data):
        password = validated_data.pop('password')  

        user = Usuario(**validated_data)
        user.set_password(password)  
        user.save()

        return user