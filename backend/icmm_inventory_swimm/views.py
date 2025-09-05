from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Rule, Device, OS, Usecase
from .serializers import RuleSerializer, DeviceSerializer, OSSerializer, UsecaseSerializer

class RuleViewSet(viewsets.ModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    @action(detail=True, methods=['post'])
    def execute_rule(self, request, pk=None):
        device = self.get_object()
        rule_id = request.data.get('rule_id')
        # Simulate execution
        return Response({'status': f'Rule {rule_id} executed on device {device.id}'})

class OSViewSet(viewsets.ModelViewSet):
    queryset = OS.objects.all()
    serializer_class = OSSerializer

class UsecaseViewSet(viewsets.ModelViewSet):
    queryset = Usecase.objects.all()
    serializer_class = UsecaseSerializer

    @action(detail=False, methods=['post'])
    def perform(self, request):
        device_id = request.data.get('device_id')
        usecase_type = request.data.get('type')
        # Simulate usecase execution
        return Response({'status': f'{usecase_type} usecase performed for device {device_id}'})