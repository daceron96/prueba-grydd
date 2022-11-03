from django.contrib import admin
from .models import Company, CompanyPoint, AccessHours, AccessHistory

admin.site.register(Company)
admin.site.register(CompanyPoint)
admin.site.register(AccessHours)
admin.site.register(AccessHistory)
