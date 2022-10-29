from rest_framework import serializers
from apps.core.models import Address, Location

class AddressSerializer(serializers.ModelSerializer):

  class Meta:
    model = Address
    exclude = ['id']

class LocationSerializer(serializers.ModelSerializer):

  class Meta:
    model = Location
    exclude = ['id']