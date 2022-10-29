from django.http import JsonResponse
from rest_framework import status, viewsets
from apps.core.api.serializers import AddressSerializer, LocationSerializer
from .serializers import UserSerializer, PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
  serializer_class = PersonSerializer

  def get_queryset(self, pk=None):
    if pk is None:
      return self.get_serializer().Meta.model.objects.filter(state = True)
    else:
      return self.get_serializer().Meta.model.objects.filter(id=pk,state = True).first()
    
  
  def create(self, request):
    errors = {}
    print('aca')
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
      return JsonResponse({'message':'Usuario registrado correctamente'}, status = status.HTTP_201_CREATED)

    return JsonResponse(errors, status = status.HTTP_400_BAD_REQUEST)
