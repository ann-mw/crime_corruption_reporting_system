from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

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
    reporter = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    report_anonymously = models.BooleanField(default=False)



    def __str__(self):
        return self.title




