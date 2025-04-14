from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    contact_number = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class CrimeRecord(models.Model):
    REPORT_TYPES = [
        ('crime', 'Crime'),
        ('corruption', 'Corruption'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date_occurred = models.DateTimeField()
    status = models.CharField(max_length=20, choices=REPORT_TYPES, default='crime')
    reporter = models.ForeignKey('UserProfile', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title