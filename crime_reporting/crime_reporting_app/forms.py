from django import forms
from .models import CrimeRecord
from .models import UserProfile

class CrimeReportForm(forms.ModelForm):
    

    class Meta:
        model = CrimeRecord
        fields = ('title', 'description', 'location', 'date_occurred', 'status','report_anonymously')
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


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'phone_number', 'address')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phone_number': 'Phone Number',
            'address': 'Address'
        }
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3})
        }