from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Vehicle

@receiver(post_save, sender=Vehicle)
def create_driver_account(sender, instance, created, **kwargs):
    if created:
        user = User.objects.create(username=instance.plugged_number)
        user.set_password(instance.driver)
        user.save()

