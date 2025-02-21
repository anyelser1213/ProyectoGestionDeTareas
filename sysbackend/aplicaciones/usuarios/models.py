import os
import shutil #libreria para borrar carpetas esten o no llenas
from django.conf import settings

from sysbackend.settings import MEDIA_URL, STATIC_URL, AUTH_USER_MODEL
from django.db import models

#Estos dos modelos son para crear permisos personalizados
from django.contrib.auth.models import Permission,Group
from django.contrib.contenttypes.models import ContentType


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete


##################################################################################################
####################### MODELO USER MANAGER ####################################################


class UsuarioManager(BaseUserManager):

    def create_user(self,email, password=None, admin = False,is_superuser =False):
        print("Creamos Usuario Normal")
        #if not email:
        #    raise ValueError('El usuario debe tener un correo electronico')

        usuario = self.model(
            
            email = email,
            password = password,
            #admin =admin,
            #is_superuser = is_superuser,
        )

        #aqui encriptamos la clave para no guardar en texto plano
        print("ENCRIPTAMOS", password)
        usuario.set_password(password)
        usuario.admin = admin
        usuario.is_superuser = is_superuser
        usuario.save()
        return usuario
    
    

    #Funcion para crear un superusuario
    def create_superuser(self,email,password):
        print("Creamos superusuario")

        usuario = self.model(
            
            email = email,
            password = password,
            #admin =admin,
            #is_superuser = is_superuser,
        )
        """
        usuario = self.create_user(
            email = email,  
            username = username,
            password = password,
            admin =admin,
            is_superuser = is_superuser
        )
        """

        print("ENCRIPTAMOS EN SUPERUSER", password)
        usuario.set_password(password)
        usuario.is_superuser = True #Es superusuario
        usuario.admin = True #Acceso a todo
        usuario.save()
        
        
        #migrupo = Roles.objects.get(name=str("LIDER"))
        #self.groups.add(migrupo)
        #self.groups.add(migrupo)


        return usuario






################################################################################################


# Heredamos de AbstractBaseUser para adaptarlo a nuestro gusto
class Usuarios(AbstractBaseUser,PermissionsMixin):



    nacionalidad = [
        
        ('venezolano','Venezolano'),
    ]

    

    id = models.AutoField(primary_key=True)


    ##Debes hacer la verificacion del email 
    email = models.EmailField("email",unique=True, null=True,blank=True)
    telefono = models.CharField("Telefono", max_length=50,blank=True,null=True)
    
    #ESTO ES ADMINISTRATIVO
    activo = models.BooleanField(default=True)#Para poder ingresar al sistema  
    is_superuser = models.BooleanField(default=False)#Este es superusuario
    admin = models.BooleanField(default=False)#Para poder ingresar al admin de django
    fecha_creacion = models.DateTimeField(auto_now_add=True) 
    ultimo_ingreso = models.DateTimeField('fecha ultimo ingreso', auto_now=True)
    
    


    
    #imagenFondoEscritorio = models.ImageField("Imagen de Escritorio", upload_to=direccion_usuarios, max_length=200,blank=True,null=True)
    
    #Para enlazar al manager que has creado
    objects = UsuarioManager()

    USERNAME_FIELD = 'email'  #PARA ESTABLECER ESTE COMO UNICO Y CON EL QUE SE ACCEDE AL SISTEMA
    #REQUIRED_FIELDS = ['email'] # Campos obligatorios(los pide cuando los creas por consola)

    def __str__(self):
        return f'{self.email}'
    
    
    
    #para verificar si un usuario es administrador o no(Para entrar en el admin)
    @property
    def is_staff(self):
         # "Is the user a member of staff?"
         if self.activo:
            return self.admin
         return False
     

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        
        super(Usuarios, self).save(*args, **kwargs)
        
        
        
        print(self.id,"Guardamos al usuario : ", self.email)
        #print(self.imagenPerfil," ",self.imagenPerfil.url)




        #print("Gruepo asignado: ",migrupo," Permisos:",self.get_group_permissions())



    class Meta:
        verbose_name = '1.Usuario'
        verbose_name_plural = '1.Usuarios'
        db_table = 'usuarios'
        
        permissions = [
            #(Lo que se guarda en bases de datos, lo que se ve al usuario)
            #Permisos para master y gerente
            #("permisoscompletos", "Permisoscompletos"),
            
            
            
            
            
            
        ]#Fin de los permisos




####################################################################################
