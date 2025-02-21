from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views_class import * 

app_name ="usuarios"

urlpatterns = [


    #CRUD VIEW CLASS
    path('usuarios/', UserListCreateView.as_view(), name='user-list-create'),
    path('usuarios/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy'),




    
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)