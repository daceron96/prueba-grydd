from rest_framework import status,viewsets
from rest_framework.response import Response
from .serializers import CompanySerializer, CompanyListSerializer, CompanyPointSerializer, AccessHourPointSerializer
from apps.core.api.serializers import AddressSerializer, LocationSerializer
from apps.company.models import CompanyPoint

class CompanyViewSet(viewsets.ModelViewSet):
  serializer_class = CompanySerializer

  def get_queryset(self):
    self.queryset = self.get_serializer().Meta.model.objects.filter(state = True)
    return self.queryset

  def list(self, request):
    company_serializer = CompanyListSerializer(self.get_queryset(), many = True)
    return Response(company_serializer.data, status = status.HTTP_200_OK)

  def create(self, request):
    errors = {}
    serializer_company = self.serializer_class(data = request.data['company'])
    serializer_address = AddressSerializer(data = request.data['address'])
    serializer_location = LocationSerializer(data = request.data['location'])

    if not serializer_company.is_valid():
      errors.update(serializer_company.errors)

    if not serializer_address.is_valid():
      errors.update(serializer_address.errors)

    if not serializer_location.is_valid():
      errors.update(serializer_location.errors)

    if not errors:
      address = serializer_address.save()
      location = serializer_location.save()
      serializer_company.create(serializer_company.validated_data, address, location)
      company = CompanyListSerializer(serializer_company.data)
      return Response(company.data, status = status.HTTP_201_CREATED)

    return Response(errors, status = status.HTTP_400_BAD_REQUEST)


class CompanyPointViewSet(viewsets.ModelViewSet):
  serializer_class = CompanyPointSerializer

  def get_queryset(self):
    pk = self.request.GET.get('nit')
    if pk is None:
      return self.get_serializer().Meta.model.objects.filter(state = True)
    else:
      return self.get_serializer().Meta.model.objects.filter(company__nit=pk,state = True)
    
  def list(self, request):
    point_serializer = self.serializer_class(self.get_queryset(), many = True)
    return Response(point_serializer.data, status = status.HTTP_200_OK)

  def create(self, request):
    errors = {}
    serializer_point= self.serializer_class(data = request.data['point'])
    serializer_address = AddressSerializer(data = request.data['address'])

    if not serializer_point.is_valid():
      errors.update(serializer_point.errors)

    if not serializer_address.is_valid():
      errors.update(serializer_address.errors)

    if not errors:
      address = serializer_address.save()
      serializer_point.create(serializer_point.validated_data, address)
      serializer_point.data.update(serializer_address.data)
      data = {}
      data.update(serializer_point.data)
      data['address'] = serializer_address.data
      return Response(data, status = status.HTTP_201_CREATED)

    return Response(errors, status = status.HTTP_400_BAD_REQUEST)

class AccessHourViewSet(viewsets.ModelViewSet):

  serializer_class = AccessHourPointSerializer
  
  def get_queryset(self):
    pk = self.request.GET.get('idPoint')
    self.queryset = self.get_serializer().Meta.model.objects.filter(companyPoint__pk = pk)
    return self.queryset

  def list(self, request):
    access_serializer = self.serializer_class(self.get_queryset(), many = True)
    return Response(access_serializer.data, status = status.HTTP_200_OK)

  def create(self, request):
    access_serializer= self.serializer_class(data = request.data)
    companyPoint = CompanyPoint.objects.get(pk = request.data['companyPoint'])
    if access_serializer.is_valid():
      
      access_serializer.create(access_serializer.validated_data, companyPoint)
      return Response(access_serializer.data, status = status.HTTP_200_OK)
    return Response(access_serializer.errors, status= status.HTTP_400_BAD_REQUEST)
