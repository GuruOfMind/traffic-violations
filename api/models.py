from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Vehicle(models.Model):
    plugged_number = models.CharField(max_length=55, primary_key=True)
    driver = models.CharField(max_length=100)
    type = models.CharField(blank=True, max_length=100)
    category = models.CharField(blank=True, max_length=100)
    production_date = models.DateField(blank=True)
    registration_date = models.DateField(blank=True)
    is_cross_out = models.BooleanField(default=False)
    def __str__(self) -> str:
        return "Vehicle: " + str(self.plugged_number) + ", Driver: " + str(self.driver)

    def get_absolute_url(self):
        return f"/vehicles/{self.plugged_number}/"

class Violation(models.Model):
    violation_type = models.CharField(max_length=255)
    tax = models.DecimalField(decimal_places=3, max_digits=12)

    def __str__(self):
        return self.violation_type
    
    def get_absolute_url(self):
        return f"/violations/{self.id}/"

class VehicleViolationLog(models.Model):
    plugged_number = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    violations_id = models.ForeignKey(Violation, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_created=True)
    location = models.CharField(max_length=255)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return "Vehicle: " + str(self.plugged_number) + ', Violation: ' + str(self.violations_id)
    
    def get_absolute_url(self):
        return f"/api/logs/{str(self.id)}"
        # return reverse("logs", kwargs={"id": self.id})

