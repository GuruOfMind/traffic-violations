from django.shortcuts import render
from rest_framework import generics, viewsets

from api_app.models import VehiclesLog, ViolationLog, Violations
from api_app.serializers import VehicleSerializer, ViolationLogSerializer, ViolationsTypeSerializer

'''
    Vehicles-related views (endpoints)
'''
# create vehicle new entry
class VehiclesCreateApiView(generics.CreateAPIView):
    queryset = VehiclesLog.objects.all()
    serializer_class =VehicleSerializer

# get all vehicles 
class VehiclesListApiView(generics.ListAPIView):
    queryset = VehiclesLog.objects.all()
    serializer_class =VehicleSerializer

# get one vehicles 
class VehiclesGetApiView(generics.RetrieveAPIView):
    queryset = VehiclesLog.objects.all()
    serializer_class =VehicleSerializer

# update one vehicle
class VehiclesUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = VehiclesLog.objects.all()
    serializer_class =VehicleSerializer

# delete a vehicle
class VehiclesDeleteApiView(generics.DestroyAPIView):
    queryset = VehiclesLog.objects.all()
    serializer_class =VehicleSerializer

'''
    violation types related endpoints
'''
class ViolationsViewSet(viewsets.ModelViewSet):
    queryset = Violations.objects.all()
    serializer_class = ViolationsTypeSerializer

class ViolationLogViewSet(viewsets.ModelViewSet):
    queryset = ViolationLog.objects.all()
    serializer_class = ViolationLogSerializer
    