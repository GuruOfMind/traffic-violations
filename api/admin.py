from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from .models import Vehicle, VehicleViolationLog, Violation

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('plugged_number', 'driver', 'type', 'category', 'is_cross_out')
    list_filter = (  'type', 'category', 'is_cross_out')
    search_fields = ('plugged_number', 'driver', 'category')

class ViolationsAdmin(admin.ModelAdmin):
    list_display = ('violation_type', 'tax')
    search_fields = ('violation_type', 'tax')


class VehicleViolationAdmin(admin.ModelAdmin):
    list_display = ('pluged_number', 'driver', 'violation', 'date', 'location', 'is_paid')

    def get_queryset(self, obj):
        qs = super(VehicleViolationAdmin, self).get_queryset(obj)
        return qs.prefetch_related('plugged_number', 'violations_id')

    def driver(self, obj):
        return obj.plugged_number.driver
    
    def pluged_number(self, obj):
        return obj.plugged_number.plugged_number

    def violation(self, obj):
        return obj.violations_id.violation_type
    
    list_filter = ( 'location', 'is_paid', ('date', DateFieldListFilter))
    search_fields = ('plugged_number__plugged_number','plugged_number__driver', 'location')

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Violation, ViolationsAdmin)
admin.site.register(VehicleViolationLog, VehicleViolationAdmin)