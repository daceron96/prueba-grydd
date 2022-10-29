from django.http import JsonResponse
from rest_framework import status,viewsets
from rest_framework.response import Response
from .serializers import CompanySerializer, CompanyListSerializer, CompanyPointSerializer
from apps.core.api.serializers import AddressSerializer, LocationSerializer

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
      return JsonResponse({'message':'Compañia creada exitosamente'}, status = status.HTTP_201_CREATED)

    return JsonResponse(errors, status = status.HTTP_400_BAD_REQUEST)


class CompanyPointViewSet(viewsets.ModelViewSet):
  serializer_class = CompanyPointSerializer

  def get_queryset(self):
    pk = self.request.GET.get('id')
  
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
      return JsonResponse({'message':'Compañia creada exitosamente'}, status = status.HTTP_201_CREATED)

    return JsonResponse(errors, status = status.HTTP_400_BAD_REQUEST)
