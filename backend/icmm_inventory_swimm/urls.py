from django.urls import path, include
from rest_framework import routers
from .views import RuleViewSet, DeviceViewSet, OSViewSet, UsecaseViewSet

router = routers.DefaultRouter()
router.register(r'rules', RuleViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'os', OSViewSet)
router.register(r'usecases', UsecaseViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]