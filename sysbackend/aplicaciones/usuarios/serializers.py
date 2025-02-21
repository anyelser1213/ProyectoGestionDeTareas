from rest_framework import serializers
from django.contrib.auth.models import User
from aplicaciones.usuarios.models import Usuarios

from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'telefono', 'password', 'activo']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):

        print("Entramos aqui...")
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.activo = True
        #user.admin = True
        #user.is_superuser = True
        user.save()
        return user

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'telefono', 'activo', 'is_staff', 'fecha_creacion', 'ultimo_ingreso']