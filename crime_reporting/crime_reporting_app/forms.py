from django import forms
from .models import CrimeRecord

class CrimeReportForm(forms.ModelForm):
    class Meta:
        model = CrimeRecord
        fields = ('title', 'description', 'location', 'date_occurred', 'status')
        widgets = {
            'date_occurred': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'title': 'Report Title',
            'description': 'Report Details',
            'location': 'Location of Incident',
            'date_occurred': 'Date and Time of Incident',
            'status': 'Report Type'
        }
        help_texts = {
            'title': 'Brief description of the incident',
            'description': 'Provide as much detail as possible',
            'location': 'Exact location where the incident occurred',
            'date_occurred': 'When did the incident occur?',
            'status': 'Select whether this is a crime or corruption report'
        }