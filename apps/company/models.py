from email.policy import default
from django.db import models
from apps.core.models import Address, Location

class Company(models.Model):

  nit = models.CharField(max_length = 100, blank=False,primary_key = True)
  icon = models.ImageField(upload_to='icons/', blank=True)
  companyName = models.CharField(max_length=100, blank=False, null=False)
  tradeName = models.CharField(max_length=100, blank=False, null=False)
  address = models.ForeignKey(Address, on_delete = models.CASCADE, null = True)
  phone = models.CharField(max_length=100, blank=False, null=False)
  email = models.EmailField(max_length=100, blank=False, null=False)
  webSite = models.URLField(max_length=100, blank=False, null=False)
  location = models.ForeignKey(Location, on_delete=models.CASCADE, null = True)
  state = models.BooleanField(default=True)
  def __str__(self):
    return self.nit 

class CompanyPoint(models.Model):

  name = models.CharField(max_length=100, blank=False, null=False)
  address = models.ForeignKey(Address, on_delete = models.CASCADE)
  email = models.EmailField(max_length=100, blank=False, null=False)
  company = models.ForeignKey(Company, on_delete=models.CASCADE)
  geolocation = models.CharField(max_length = 100, blank=True, null=True)
  state = models.BooleanField(default=True)


  def __str__(self):
    return self.name 

class AccessHours(models.Model):

  startTime = models.TimeField(auto_now=False, auto_now_add=False)
  endTime = models.TimeField(auto_now=False, auto_now_add=False)
  companyPoint = models.ForeignKey(CompanyPoint, on_delete = models.CASCADE)

  def __str__(self):
    return f'{self.id}'