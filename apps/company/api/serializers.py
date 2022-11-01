from rest_framework import serializers
from apps.company.models import Company, CompanyPoint, AccessHours
from apps.core.api.serializers import AddressSerializer, LocationSerializer

class CompanySerializer(serializers.ModelSerializer):

  address = AddressSerializer(read_only = True)
  location = LocationSerializer(read_only = True)

  class Meta:
    model = Company
    exclude = ['state']
  
  def create(self, validated_data, address, location):
    company = Company(**validated_data)
    company.address = address
    company.location = location
    company.save()
    return company  
  
class CompanyListSerializer(serializers.ModelSerializer):

  class Meta:
    model = Company
    fields = ['nit','companyName', 'tradeName', 'phone', 'email']


class CompanyPointSerializer(serializers.ModelSerializer):
  address = AddressSerializer(read_only = True)

  class Meta:
    model = CompanyPoint
    exclude = ['state']

  def create(self, validated_data, address):
    point = CompanyPoint(**validated_data)
    point.address = address
    point.save()
    return point

class AccessHourPointSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = AccessHours
    exclude = ['companyPoint']

  def create(self, validated_data, point):
    access = AccessHours(**validated_data)
    access.companyPoint = point
    access.save()
    return access