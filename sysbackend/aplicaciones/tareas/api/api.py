from itertools import chain
import json
from datetime import datetime

from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from aplicaciones.bienesapp.models import *
from aplicaciones.bienesapp.apis.api_bienes_muebles.serializers import *




@api_view(['POST'])
def obtener_subcategorias_de_bienes_muebles_api_view(request):
    data = request.data  # DRF maneja la lectura del cuerpo de la solicitud automáticamente
    #print("Datos recibidos:", data)
    selected_option = data.get('categoria_general')

    if selected_option:
        # Filtra las gerencias basadas en la opción seleccionada
        subcategorias = Subcategoria.objects.filter(categoria_general__id=int(selected_option))  # Ajusta la relación según tu modelo
        serializer = SubcategoriasBienesMueblesSerializer(subcategorias, many=True)
        return Response(serializer.data)
    else:
        return Response({'error': 'No se proporcionó una opción válida'}, status=400)
    

@api_view(['POST'])
def obtener_categorias_especificas_de_bienes_muebles_api_view(request):
    data = request.data  # DRF maneja la lectura del cuerpo de la solicitud automáticamente
    #print("Datos recibidos:", data)
    selected_option = data.get('subcategoria')

    if selected_option:
        # Filtra las gerencias basadas en la opción seleccionada
        subcategorias = CategoriaEspecifica.objects.filter(subcategoria__id=int(selected_option))  # Ajusta la relación según tu modelo
        serializer = SubcategoriasBienesMueblesSerializer(subcategorias, many=True)
        return Response(serializer.data)
    else:
        return Response({'error': 'No se proporcionó una opción válida'}, status=400)