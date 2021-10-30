from django.contrib.auth.backends import UserModel
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
    violation = serializers.CharField(source="violations_id.violation_type")
    tax = serializers.CharField(source="violations_id.tax")
    driver = serializers.CharField(source="plugged_number.driver")
    class Meta:
        model = VehicleViolationLog
        # fields = '__all__'
        exclude = ('violations_id', )


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user
    class Meta:
        model = UserModel
        fields = ( "id", "username", "password", )