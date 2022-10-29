from rest_framework.routers import DefaultRouter
from apps.user.api.api import PersonViewSet

router = DefaultRouter()

router.register(r'person', PersonViewSet, basename='person')

urlpatterns = router.urls