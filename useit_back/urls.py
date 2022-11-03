from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from apps.user.urls import authentication_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('apps.company.api.routers')),
    path('api/',include('apps.user.api.routers')),
    path('api/', include(authentication_patterns)),

]

