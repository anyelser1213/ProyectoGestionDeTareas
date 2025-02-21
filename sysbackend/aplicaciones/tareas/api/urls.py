from django.urls import path
from aplicaciones.bienesapp.apis.api_bienes_muebles.api import *


urlpatterns = [

    #Normal
    #APIS PARA BIENES MUEBLES
    path('obtenersubcategoriasbienesmuebles/',obtener_subcategorias_de_bienes_muebles_api_view,name='obtener_subcategorias_bienes_muebles'),
    path('obtenercategoriasespecificasbienesmuebles/',obtener_categorias_especificas_de_bienes_muebles_api_view,name='obtener_categorias_especificas_bienes_muebles'),

    
]