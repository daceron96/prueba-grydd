from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from apps.user.urls import authentication_patterns
from django.views.static import serve
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('apps.company.api.routers')),
    path('api/',include('apps.user.api.routers')),
    path('api/', include(authentication_patterns)),

]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root' : settings.MEDIA_ROOT
    })
]