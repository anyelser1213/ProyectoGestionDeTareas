from django.db import models

#Aplicacion personalizada del usuario
from aplicaciones.usuarios.models import Usuarios

class Tareas(models.Model):

    usuario = models.ForeignKey(Usuarios,on_delete=models.CASCADE,null=True,blank=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    completado = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo