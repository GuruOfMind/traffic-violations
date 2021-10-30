from django.contrib.auth import authenticate, login
from django.http.response import Http404
from requests.models import Response
from rest_framework import viewsets
from rest_framework.views import APIView
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
    filterset_fields = ('plugged_number', 'plugged_number__driver', 'is_paid')

# class PaymentView(APIView):
#     def get_object(self, pk):
#         try:
#             return VehicleViolationLog.objects.get(pk=pk)
#         except VehicleViolationLog.DoesNotExist:
#             raise Http404

#     def put(self, request, pk, format=None):
#         violation = self.get_object(pk)
#         serializer = VehicleViolationLogSerializer(violation, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)