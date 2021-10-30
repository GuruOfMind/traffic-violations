from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
import django_filters.rest_framework as filters

from api.models import Vehicle, VehicleViolationLog, Violation
from api.serializers import UserSerializer, VehicleSerializer, VehicleViolationLogSerializer, ViolationTypeSerializer

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
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data('plugged_number')
            raw_password = form.cleaned_data.get('driver')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return "good"
        else:
            form = UserCreationForm()
        return "bad"


class CreateUserView(CreateAPIView):

    model = User()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer
