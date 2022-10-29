from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView

from .api.serializers import CustomTokenObtainPairSerializer, PersonLoginSerializer

class Login(TokenObtainPairView):
  serializer_class = CustomTokenObtainPairSerializer
  
  def post(self, request, *args, **kwargs):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password )
    if user:
      login_serializer = self.serializer_class(data=request.data)
      if login_serializer.is_valid():
        try:
          user_serializer = PersonLoginSerializer(user.person).data
          person = user.person
          person.token = login_serializer.validated_data.get('access')
          person.save()
        except:
          user_serializer = {'names':'SuperAdmin'}
          
        return Response({
          'token' : login_serializer.validated_data.get('access'),
          'refresh-token' : login_serializer.validated_data.get('refresh'),
          'user' : user_serializer,
          'message' : 'Inicio de sesion exitoso'
        }, status = status.HTTP_200_OK)
      return Response({'error':'Contraseña o número de documento incorrecto'},status=status.HTTP_400_BAD_REQUEST)
    return Response({'error':'Contraseña o número de documento incorrecto'},status=status.HTTP_400_BAD_REQUEST)

