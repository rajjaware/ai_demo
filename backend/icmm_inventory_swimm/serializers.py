from rest_framework import serializers
from .models import Rule, Device, OS, Usecase

class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    icmm_rules = RuleSerializer(many=True, read_only=True)
    class Meta:
        model = Device
        fields = '__all__'

class OSSerializer(serializers.ModelSerializer):
    class Meta:
        model = OS
        fields = '__all__'

class UsecaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usecase
        fields = '__all__'