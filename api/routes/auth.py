# Librerias principales
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

# authenticadores
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils import timezone

# Serializer Principal
from ..model.serializer import UserRegisterSerializer

# Tablas de Tyni
from ..tablas.jsontablas import tablaData

# Importacion de Mongo
from ..mongo.client import collection

# ----- Endpoint Tempo -------
def time():
    timeactual = timezone.now()
    timeBase = timezone.localtime(timeactual)
    timestring = timeBase.strftime("%I:%M:%S:%p")

    return timestring

# --- ENDPOINT REGISTRO ---
@api_view(['POST'])
@permission_classes([AllowAny]) # Permite que cualquiera se registre sin estar logueado
def register(request):
    serializer = UserRegisterSerializer(data=request.data)
    
    if serializer.is_valid():
        # 1. Guardamos el usuario (se encripta pass automáticamente)
        user = serializer.save()
        
        # 2. Creamos (o recuperamos) el token para este usuario
        token, created = Token.objects.get_or_create(user=user)
        time_str = time() 

        datos_a_guardar = {
            "user":serializer.data,
            "token": token.key,
            "created_at":time_str
        }

        datos = tablaData.insert(datos_a_guardar)

        mongo = collection.insert_one(datos_a_guardar)
        
        # 3. Devolvemos usuario y token
        return Response({
            "user": serializer.data,
            "token": token.key,
            "message": "Usuario creado exitosamente",
            "datos": f"Guaradados {datos} {mongo}"
        }, status=status.HTTP_201_CREATED)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- ENDPOINT LOGIN ---
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):

    identificador = request.data.get('username') or request.data.get('email')
    password = request.data.get('password')
    
    if not identificador or not password:
        return Response({"error": "Faltan credenciales"}, status=status.HTTP_400_BAD_REQUEST)

    usuario_para_autenticar = identificador

    # Si parece un email (tiene @), buscamos el username real asociado a ese email
    if '@' in identificador:
        try:
            # Buscamos el usuario por email
            user_obj = User.objects.get(email=identificador)
            # Si existe, usamos su username real para la autenticación
            usuario_para_autenticar = user_obj.username
        except User.DoesNotExist:
            pass

    # Autenticamos usando el username real (que obtuvimos del email o del input directo)
    user = authenticate(username=usuario_para_autenticar, password=password)

    if user is not None:
        # Credenciales correctas -> Generamos o recuperamos token
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "token": token.key,
            "user_id": user.pk,
            "email": user.email
        }, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)
