from rest_framework import serializers
from .models import Tareas

class TareasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tareas
        fields = '__all__'
        # fields = ['id', 'usuario', 'titulo', 'descripcion', 'completado', 'creado', 'actualizado']
        # Si quieres un serializador para crear tareas y no quieres que el usuario pueda modificar los campos 'creado' y 'actualizado'
        # fields = ['usuario', 'titulo', 'descripcion', 'completado'] # No incluyas 'id' porque se genera automáticamente