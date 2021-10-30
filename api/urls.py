from django.urls import include, path
from rest_framework import routers

from api.views import CreateUserView, VehicleViolationLogViewSet, VehiclesViewSet, ViolationsViewSet

router = routers.DefaultRouter()
router.register(r'vehicles', VehiclesViewSet, basename='vehicles')
router.register(r'violations', ViolationsViewSet, basename='violations')
router.register(r'vehicle-violation-logs', VehicleViolationLogViewSet, basename='vehicle-violation-logs')

urlpatterns = [
   path('', include(router.urls)),
   path('register/', CreateUserView.as_view(), name="register")
]