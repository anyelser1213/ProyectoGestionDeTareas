from rest_framework import generics
from .models import Usuarios
from .serializers import CustomUserSerializer  

class UserListCreateView(generics.ListCreateAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = CustomUserSerializer  

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = CustomUserSerializer  