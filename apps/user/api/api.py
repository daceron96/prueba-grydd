from rest_framework.response import Response
from rest_framework import status, viewsets
from apps.core.api.serializers import AddressSerializer, LocationSerializer
from .serializers import UserSerializer, PersonSerializer, PersonSerializerList
from rest_framework.generics import GenericAPIView
from apps.company.models import AccessHistory
from apps.user.models import Person

from datetime import datetime


class PersonViewSet(viewsets.ModelViewSet):
  serializer_class = PersonSerializer

  def get_queryset(self):
    nit = self.request.GET.get('nit')
    query = self.get_serializer().Meta.model.objects.filter(companyPoint__company__nit = nit)
    return query
  
  def list(self, request):
    list_serializer = PersonSerializerList(self.get_queryset(), many = True)
    return Response(list_serializer.data, status = status.HTTP_200_OK)

  
  def create(self, request):
    errors = {}
    serializer_person = self.serializer_class(data = request.data['person'])
    serializer_address = AddressSerializer(data = request.data['address'])
    serializer_location = LocationSerializer(data = request.data['location'])

    serializer_user = UserSerializer(data = {})
    try:
      serializer_user = UserSerializer(data = {'username' : request.data['person']['identifier'], 'password' : request.data['person']['password']})
    except:
      pass

    if not serializer_person.is_valid():
      errors.update(serializer_person.errors)

    if not serializer_address.is_valid():
      errors.update(serializer_address.errors)

    if not serializer_user.is_valid():
      errors.update(serializer_user.errors)

    if not serializer_location.is_valid():
      errors.update(serializer_location.errors)

    if not errors :
      address = serializer_address.save()
      location = serializer_location.save()
      user = serializer_user.save()
      serializer_person.create(serializer_person.validated_data, address, location, user )
      person = PersonSerializerList(serializer_person.data)
      return Response(person.data, status = status.HTTP_201_CREATED)

    return Response(errors, status = status.HTTP_400_BAD_REQUEST)


class ValidateAccessPerson(GenericAPIView):

  def get(self, request):
    identifier = request.GET.get('identifier')
    person = Person.objects.get(identifier = identifier)
    accessHistory = AccessHistory.objects.filter(person = person, state=True).first()
    if(accessHistory == None):
      if(not person.state):
        return Response({
          'access':False, 
          'message': 'Esta Persona esta suspendida'
          }, status = status.HTTP_401_UNAUTHORIZED)

      now = datetime.now().time()
      accessHour = person.accessHour
      if(accessHour.startTime <= now and accessHour.endTime >= now):
        access = AccessHistory.objects.create(
          person = person,
          accessHour= accessHour,
          user = request.user,
        )
        person.accessHistory = access
        person.save()
        return Response({
            'access':True, 
        'message':'Ingreso exitoso'
        }, status = status.HTTP_200_OK)
      return Response({
        'access':False, 
        'message':'La persona esta fuera de su horario de acceso'
        }, status = status.HTTP_401_UNAUTHORIZED)
    
    return Response({
      'access' : False,
      'message' : 'Esta persona ya tiene un ingreso activo' 
    }, status = status.HTTP_400_BAD_REQUEST)
