from rest_framework.routers import DefaultRouter
from .api import CompanyViewSet, CompanyPointViewSet, AccessHourViewSet

router = DefaultRouter()

router.register(r'company', CompanyViewSet, basename='company')
router.register(r'point', CompanyPointViewSet, basename='company_point')
router.register(r'access', AccessHourViewSet, basename='point_access')

urlpatterns = router.urls