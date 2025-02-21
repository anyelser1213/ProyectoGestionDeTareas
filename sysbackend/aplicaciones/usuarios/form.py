from django import forms
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ClearableFileInput, ModelForm, widgets
from aplicaciones.usuarios.models import Usuarios



###################### AQUI COMIENZAN LOS FORMULARIOS PARA USUARIOS ##########################################


#Este es u usuario personalizado para el modelo usuarios
class UsuarioPersonalizadoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        #usuario_id = kwargs.pop('usuario')
        #self.usuarioID = kwargs.pop('user')
        super(UsuarioPersonalizadoForm, self).__init__(*args, **kwargs)
        print("Formulario Usuario Personalizado: \n")
        #print("usuario: ",usuario_id)
        #print("usuario ID: ",self.usuarioID.id)

        #self.fields['creado_por'].empty_label = None
        #self.fields['creado_por'].queryset = Usuarios.objects.filter(id=self.usuarioID.id)

        #self.fields['imagen'].widget.attrs.update({'class': 'form-control ' })

    class Meta:

        model = Usuarios
        #fields = "__all__"

        #Estos campos no son necesarios en el registro normal de usuarios
        exclude = ('user_permissions','groups','last_login','activo','admin','is_superuser','password','nacionalidad')
        widgets = {
            #"nombre": forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa nombre de calidad'}),
            #"direccion": forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter company address'}),
            #"descripcion": forms.Textarea(attrs={'class': 'form-control border-input','rows':'3','placeholder':'Enter company information'}),
            #"color": forms.TextInput(attrs={'type': 'color', 'class':'form-control oculto2'}),
            "imagen_perfil":forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'Ingresa imagen'}),
            "cedula": forms.TextInput(attrs={'class': 'form-control ','placeholder':'Ingresa tu cedula'}),
            "nombre_principal": forms.TextInput(attrs={'class': 'form-control ','placeholder':'Ingresa tu nombre principal'}),
            "nombre_secundario": forms.TextInput(attrs={'class': 'form-control ','placeholder':'Ingresa tu nombre secundario'}),
            "apellido_principal": forms.TextInput(attrs={'class': 'form-control ','placeholder':'Ingresa tu apellido principal'}),
            "apellido_secundario": forms.TextInput(attrs={'class': 'form-control ','placeholder':'Ingresa tu apellido secundario'}),
            "tipo_usuario": forms.Select(attrs={'class': 'form-control' }),
            "cargo_usuario": forms.Select(attrs={'class': 'form-control' }),
            "email": forms.EmailInput(attrs={'placeholder': 'Ingresa tu email','class': 'form-control'}),
            "telefono": forms.TextInput(attrs={'class': 'form-control ','placeholder':'Ingresa tu n° telefonico'}),
            "direccion": forms.TextInput(attrs={'class': 'form-control ','placeholder':'Ingresa tu dirección'}),
            #"imagenEmpresa":forms.ClearableFileInput(attrs={'class': 'form-control oculto','placeholder':'Enter company image'}),
            #"videoEmpresa": forms.ClearableFileInput(attrs={'class': 'form-control oculto','placeholder':'Enter company video','accept':'video/*'}),
            #"creado_por": forms.Select(attrs={'class': 'form-select','style': 'display:none'  }),
        }
