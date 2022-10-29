from django.db import models

class Address(models.Model):

  street = models.CharField(max_length = 100, blank=False, null=False)
  number = models.CharField(max_length = 100, blank=False, null=False)
  district = models.CharField(max_length = 100, blank=False, null=False)
  postalCode = models.CharField(max_length = 100, blank=False, null=False)
  
  def __str__(self):
    return f'{self.id}'

class Location(models.Model):

  country = models.CharField(max_length = 100, blank=False, null=False)
  department = models.CharField(max_length = 100, blank=False, null=False)
  city = models.CharField(max_length = 100, blank=False, null=False)

  def __str__(self):
    return f'{self.id}'