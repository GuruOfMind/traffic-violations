from django.db import models

class VehiclesLog(models.Model):
    plugged_number = models.CharField(max_length=55, primary_key=True)
    driver = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    production_date = models.DateField()
    registration_date = models.DateField()
    is_cross_out = models.BooleanField(default=False)

class Violations(models.Model):
    violation_type = models.CharField(max_length=255)
    tax = models.DecimalField(decimal_places=3, max_digits=12)

    def __str__(self):
        return self.violation_type

class ViolationLog(models.Model):
    plugged_number = models.ForeignKey(VehiclesLog, on_delete=models.CASCADE)
    violations_id = models.ForeignKey(Violations, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_created=True)
    location = models.CharField(max_length=255)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.plugged_number + ' ' + self.violations_id
