from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views as vistasLogin


urlpatterns = [
    

    
    # ... otras rutas
    path('logout/', vistasLogin.logout_view, name='logout'),
    




    #Para las apis
    #path('probando/', views.Probando ,name="probando"),
    #path('api_login/', views.api_login ,name="api_login"),

    
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)