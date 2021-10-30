from rest_framework import serializers
from .models import Vehicle, VehicleViolationLog, Violation

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class ViolationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Violation
        fields = '__all__'

class VehicleViolationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleViolationLog
        fields = '__all__'
        
        