from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from .models import CrimeRecord
from .forms import CrimeReportForm
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.contrib.auth import login
from .forms import UserProfileForm


@login_required
def report_crime(request):
    if request.method == 'POST':
        form = CrimeReportForm(request.POST)
        if form.is_valid():
            crime_report = form.save(commit=False)
            if not form.cleaned_data['report_anonymously']:
                crime_report.reporter = request.user.userprofile
            crime_report.save()
            messages.success(request, 'Report submitted successfully.')
            return redirect('user_dashboard')
    else:
        form = CrimeReportForm()
    return render(request, 'crime_reporting_app/report_crime.html', {'form': form, 'title': 'Report a Crime'})

    

@login_required
def view_reports(request):
    if request.user.is_staff:
        reports = CrimeRecord.objects.all()
    else:
        try:
            profile = request.user.userprofile
            reports = CrimeRecord.objects.filter(reporter=profile)
        except UserProfile.DoesNotExist:
            reports = []

    return render(request, 'crime_reporting_app/view_reports.html', {
        'reports': reports,
        'title': 'View Reports'
    })



def register(request):
    if request.user.is_authenticated and request.user.is_staff:
        messages.error(request, "Admins cannot register.")
        return redirect('login')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create minimal UserProfile (first_name, last_name optional)
            UserProfile.objects.get_or_create(user=user)

            login(request, user)
            messages.success(request, "Registration successful! Welcome.")
            return redirect('user_dashboard')  # 👈 Go straight to dashboard
    else:
        form = UserCreationForm()

    return render(request, 'crime_reporting_app/register.html', {'form': form})



@login_required
def update_profile(request):
    profile = request.user.userprofile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('user_dashboard')  # or 'view_reports'
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'crime_reporting_app/update_profile.html', {'form': form})




@login_required
def user_dashboard(request):
    if request.user.is_staff:
        return redirect('admin:index')  # Admins go to the admin dashboard
    return render(request, 'crime_reporting_app/user_dashboard.html')

from django.shortcuts import render

def homepage(request):
    return render(request, 'crime_reporting_app/home.html')

