from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, 
                          choices=[('citizen', 'Citizen'), ('admin', 'Admin')])
    created_at = models.DateTimeField(auto_now_add=True)

class ReportCategory(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ReportStatus(models.Model):
    status_name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class CrimeReport(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    reported_date = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(ReportStatus, on_delete=models.CASCADE)
    category = models.ForeignKey(ReportCategory, on_delete=models.CASCADE)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)

class ReportStatusHistory(models.Model):
    report = models.ForeignKey(CrimeReport, on_delete=models.CASCADE)
    status = models.ForeignKey(ReportStatus, on_delete=models.CASCADE)
    changed_at = models.DateTimeField(auto_now_add=True)
    changed_by = models.ForeignKey(User, on_delete=models.CASCADE)
