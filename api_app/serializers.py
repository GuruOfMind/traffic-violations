from rest_framework import serializers
from .models import VehiclesLog, Violations, ViolationLog

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiclesLog
        fields = '__all__'
        # fields = ('plugged_number', 'driver', 'type', 'category', 'production_date', 'registration_date', 'is_cross_out')

class ViolationsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Violations
        fields = '__all__'
        # fields = ('violation_type', 'tax')

class ViolationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViolationLog
        fields = '__all__'
        # fields = ('plugged_number', 'violations_id', 'date', 'location', 'is_paid')
        