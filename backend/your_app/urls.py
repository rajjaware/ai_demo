from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RuleViewSet, DeviceViewSet, OSViewSet, UsecaseViewSet

router = routers.DefaultRouter()
router.register(r'rules', RuleViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'os', OSViewSet)
router.register(r'usecases', UsecaseViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/devices/filter/', DeviceViewSet.as_view({'get': 'filter'}), name='device-filter'),
]