from django.db import models
from apps.company.models import CompanyPoint, AccessHours
from django.contrib.auth.models import User
from apps.core.models import Location, Address

class Person(models.Model):
  identifier = models.CharField(max_length = 100, unique=True)
  names = models.CharField(max_length = 100)
  surNames = models.CharField(max_length = 100)
  companyPoint = models.ForeignKey(CompanyPoint, on_delete = models.CASCADE)
  accessHour = models.ForeignKey(AccessHours, on_delete = models.CASCADE)
  phone = models.CharField(max_length = 100)
  location = models.ForeignKey(Location, on_delete = models.CASCADE, null=True)
  email = models.EmailField(max_length = 100)
  address = models.ForeignKey(Address, on_delete = models.CASCADE, null=True)
  role = models.CharField(max_length = 10)
  state = models.BooleanField(default = True)
  user = models.OneToOneField(User, on_delete = models.CASCADE, null=True)
  token = models.CharField(max_length = 100, blank = True, null = True)

  def __str__(self):
    return self.names
