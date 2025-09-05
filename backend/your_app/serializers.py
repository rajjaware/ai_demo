from rest_framework import serializers
from .models import User, Rule, Device, OS, Usecase

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
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