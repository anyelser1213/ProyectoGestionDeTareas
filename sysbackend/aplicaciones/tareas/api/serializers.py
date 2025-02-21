from rest_framework import serializers
#from aplicaciones.bienesapp.models import Subcategoria #Esta es la subcategoria para bienes muebles
#from aplicaciones.bienesapp.models import SubcategoriaInmuebles #Esta es la subcategoria para bienes inmuebles

from aplicaciones.bienesapp.models import * #Aqui importamos todo

class CategoriasEspecificasBienesMueblesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaEspecifica
        fields = ['id', 'nombre']  # Solo incluye 'id' y 'nombre' en la respuesta


class SubcategoriasBienesMueblesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategoria
        fields = ['id', 'nombre']  # Solo incluye 'id' y 'nombre' en la respuesta



###################################################################################



####################################################################################