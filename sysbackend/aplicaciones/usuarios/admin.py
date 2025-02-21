from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Permission

from .models import *


#Con esto modificamos los titulos en el admin de django
admin.site.site_header = 'Bienes'
admin.site.index_title = 'Sistema de Bienes'
admin.site.site_title = 'BIENES'

class UserAdmin(BaseUserAdmin):
    
    ordering = ('email',)
    
    #Aqui es cuando se va a editar
    fieldsets = (
        #Aqui es para editar
        ("Informacion Esencial", {'fields': ('email','telefono', 'password')}),
        ("Permisologia", {
            'classes': ('wide',),
            'fields': ('is_superuser','admin','activo','groups','user_permissions'),
        }),
    )

    #Aqui es cuando se esta creando
    add_fieldsets = (
        ("Informacion Obligatoria", {
            'classes': ('wide',),
            'fields': ('email','telefono', 'password1', 'password2'),
        }),
        ("Informacion Importante", {
            'classes': ('wide',),
            'fields': ('activo', 'is_superuser','admin','telefono'),
            #'fields': ('activo', 'is_superuser','admin', 'cedula','plan_elegido','rol','telefono'),
        }),
        ("Permisologia", {
            'classes': ('wide',),
            'fields': ('groups','user_permissions',),
        }),
    )


    #Para indicarle al admin que campos queremos mostrar
    list_display = ('id','email','is_superuser','admin','telefono','activo','fecha_creacion','ultimo_ingreso')
    #list_display = ('username', 'email','is_superuser','admin','rol','plan_elegido')
    list_filter = ('email','activo')
    
    #Para especificar que campos van a efectuar la busqueda
    search_fields = ('email',)
    filter_horizontal = ()






#admin.site.register(TipoUsuario)
#Aqui registramos los elementos para que aparezcan en el admin de django
admin.site.register(Usuarios, UserAdmin)

admin.site.register(Permission)




"""

class CategoriaAdmin(admin.ModelAdmin):
    #readonly_fields = ('categoria', 'nombre') #Si lo colocas no se podra agregar nada
    list_display = ('nombre', 'activo',)
    ordering = ('nombre',)
    #date_hierarchy = 'created' #Sirve para ordenar por fecha de creacion


class SubcategoriaAdmin(admin.ModelAdmin):
    #readonly_fields = ('categoria', 'nombre') #Si lo colocas no se podra agregar nada
    list_display = ( 'nombre','categoria', 'activo',)
    fields = ( 'nombre','categoria','activo',)
    ordering = ('nombre',)

class VideoAdmin(admin.ModelAdmin):
    #readonly_fields = ('categoria', 'nombre') #Si lo colocas no se podra agregar nada
    list_display = ('categoria','subcategoria', 'nombre', 'activo','video')

    fields = ('categoria', 'subcategoria', 'activo', 'video') #Campos que se van a mostrar al crear un nuevo video
    ordering = ('nombre',)

class ArchivosAdmin(admin.ModelAdmin):
    #readonly_fields = ('categoria', 'nombre') #Si lo colocas no se podra agregar nada
    list_display = ('nombre','categoriaPrueba','subcategoria', 'activo','archivo')

    fields = ('categoriaPrueba', 'subcategoria', 'activo', 'archivo') #Campos que se van a mostrar al crear un nuevo video
    ordering = ('nombre',)

"""

#Modelos del proyecto
"""
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Subcategoria,SubcategoriaAdmin)
admin.site.register(Video,VideoAdmin)
admin.site.register(Archivos,ArchivosAdmin)

admin.site.register(Fondos)

 """