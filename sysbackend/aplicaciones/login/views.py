from django.conf import settings  # Importa settings
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def logout_view(request):
    print("Entrando en logout_view")
    print(f"SIMPLE_JWT: {settings.SIMPLE_JWT}")  # Accede a la configuración a través de settings
    try:
        refresh_token = request.data.get('refresh_token')
        print(f"Refresh token recibido: {refresh_token}")
        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                print(f"Token creado: {token}")
                token.blacklist()  # La línea que debería funcionar
                print("Refresh token añadido a la lista negra")
                return Response({'message': 'Refresh token revocado correctamente.'})
            except Exception as e:
                print(f"Error al revocar refresh token: {e}")  # ¡Imprime el error!
                return Response({'message': 'Error al revocar el refresh token'}, status=500)
        else:
            print("Refresh token no proporcionado")
            return Response({'message': 'Refresh token no proporcionado.'}, status=400)
    except Exception as e:
        print(f"Error general en logout_view: {e}")  # ¡Imprime el error!
        return Response({'message': 'Error al cerrar sesión.'}, status=500)