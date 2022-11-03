from django.urls import path
from .authentication import Login
from .api.api import ValidateAccessPerson
authentication_patterns = ([
    # Auth views
    path('login/',Login.as_view(), name='auth_login'),
    path('check-in/',ValidateAccessPerson.as_view(), name='validate_access'),

    # path('logout/',Logout.as_view(), name='auth_logout'),
],'authentication')