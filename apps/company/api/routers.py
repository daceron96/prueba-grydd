from rest_framework.routers import DefaultRouter
from .api import CompanyViewSet, CompanyPointViewSet

router = DefaultRouter()

router.register(r'company', CompanyViewSet, basename='company')
router.register(r'point', CompanyPointViewSet, basename='company_point')

urlpatterns = router.urls