from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Rule, Device, OS, Usecase
from .serializers import RuleSerializer, DeviceSerializer, OSSerializer, UsecaseSerializer

class RuleViewSet(viewsets.ModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer
    permission_classes = [IsAuthenticated]

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def filter(self, request):
        rule_name = request.query_params.get('rule')
        name = request.query_params.get('name')
        location = request.query_params.get('location')
        ip = request.query_params.get('ip')
        devices = Device.objects.all()
        if rule_name:
            devices = devices.filter(icmm_rules__name=rule_name)
        if name:
            devices = devices.filter(name__icontains=name)
        if location:
            devices = devices.filter(location__icontains=location)
        if ip:
            devices = devices.filter(ip__startswith=ip)
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)

class OSViewSet(viewsets.ModelViewSet):
    queryset = OS.objects.all()
    serializer_class = OSSerializer
    permission_classes = [IsAuthenticated]

class UsecaseViewSet(viewsets.ModelViewSet):
    queryset = Usecase.objects.all()
    serializer_class = UsecaseSerializer
    permission_classes = [IsAuthenticated]