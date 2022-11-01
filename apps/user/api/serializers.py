from rest_framework import serializers
from apps.core.api.serializers import AddressSerializer, LocationSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.user.models import Person
from django.contrib.auth.models import User

class PersonSerializer(serializers.ModelSerializer):
  address = AddressSerializer(read_only = True)
  location = LocationSerializer(read_only = True)

  class Meta:
    model = Person
    exclude = ['state']

  def validate_role(self, value):
    if value != 'admin' and value != 'staff':
      raise serializers.ValidationError('Selecciona un tipo de usuario')
    return value


  def create(self, validated_data, address, location, user):
    person = Person(**validated_data)
    person.address = address
    person.location = location
    person.user = user
    person.save()
    return person  

class PersonSerializerList(serializers.ModelSerializer):

  class Meta:
    model = Person
    fields = ['names','surNames','email', 'phone', 'identifier', 'role']

class UserSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = '__all__'


  def create(self, validate_data):
    user = User(**validate_data)
    user.set_password(validate_data['password'])
    user.save()
    return user

class PersonLoginSerializer(serializers.ModelSerializer):
  class Meta:
    model = Person
    fields = ['names','surNames','role']

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
  pass
