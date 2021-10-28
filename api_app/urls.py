from django.urls import include, path
from rest_framework import routers

from api_app.views import VehiclesCreateApiView, VehiclesDeleteApiView, VehiclesGetApiView, VehiclesListApiView, VehiclesUpdateApiView, ViolationLogViewSet, ViolationsViewSet

urlpatterns = [
   path('vehicles/', VehiclesListApiView.as_view(), name="vehicles_list"),
   path('vehicles/create/', VehiclesCreateApiView.as_view(), name="vehicles_create"),
   path('vehicles/<str:pk>/', VehiclesGetApiView.as_view(), name="vehicles_list"),
   path('vehicles/<str:pk>/update/', VehiclesUpdateApiView.as_view(), name="vehicle_update"),
   path('vehicles/<str:pk>/delete/', VehiclesDeleteApiView.as_view(), name="vehicle_delete"),
   path('violations/', ViolationsViewSet, name="violations_list"),
   path('logs/', ViolationLogViewSet, name="log_list"),

]