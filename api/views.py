from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
import django_filters.rest_framework as filters

from api.models import Vehicle, VehicleViolationLog, Violation
from api.serializers import VehicleSerializer, VehicleViolationLogSerializer, ViolationTypeSerializer

'''
    Vehicles-related views (endpoints)
'''
class VehiclesViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = Vehicle.objects.all()
    serializer_class =VehicleSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('plugged_number', 'driver', 'category', 'type')

'''
    violation types related endpoints
'''
class ViolationsViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = Violation.objects.all()
    serializer_class = ViolationTypeSerializer

'''
    vehicle-violations log related endpoints
'''
class VehicleViolationLogViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = VehicleViolationLog.objects.all()
    serializer_class = VehicleViolationLogSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('plugged_number', 'plugged_number__driver')
    