from django.urls import path
from .authentication import Login
authentication_patterns = ([
    # Auth views
    path('login/',Login.as_view(), name='auth_login'),
    # path('logout/',Logout.as_view(), name='auth_logout'),
],'authentication')