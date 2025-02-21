from django.urls import path
from .views_class import *

urlpatterns = [
    path('tareas/', TareasListCreateView.as_view(), name='task-list-create'),
    path('tareasUser/', TareasListCreateView2.as_view(), name='task-list-create2'),
    path('tareas/<int:pk>/', TareasRetrieveUpdateDestroyView.as_view(), name='task-retrieve-update-destroy'),
]