from rest_framework import generics
from .models import Tareas
from .serializers import TareasSerializer

class TareasListCreateView(generics.ListCreateAPIView):
    queryset = Tareas.objects.all()
    serializer_class = TareasSerializer

class TareasListCreateView2(generics.ListCreateAPIView):
    serializer_class = TareasSerializer

    def get_queryset(self):  # Usamos get_queryset en lugar de queryset
        user = self.request.user
        return Tareas.objects.filter(usuario=user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(usuario_id=user.id)  # Guarda el ID al crear una tarea

class TareasRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tareas.objects.all()
    serializer_class = TareasSerializer