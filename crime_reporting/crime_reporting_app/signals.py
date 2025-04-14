
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# crime_reporting_app/apps.py
from django.apps import AppConfig

class CrimeReportingAppConfig(AppConfig):
    name = 'crime_reporting_app'
    verbose_name = "Crime Reporting App"

    def ready(self):
        import crime_reporting_app.signals