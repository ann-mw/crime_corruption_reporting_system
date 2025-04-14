from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CrimeRecord
from .forms import CrimeReportForm

@login_required
def report_crime(request):
    if request.user.is_staff:
        messages.error(request, "Admins can only view records in the admin dashboard")
        return redirect('admin:index')
    
    if request.method == 'POST':
        form = CrimeReportForm(request.POST)
        if form.is_valid():
            crime_record = form.save(commit=False)
            crime_record.reporter = request.user
            crime_record.save()
            messages.success(request, "Crime report submitted successfully")
            return redirect('view_reports')
    else:
        form = CrimeReportForm()
    
    return render(request, 'crime_reporting_app/report_crime.html', {
        'form': form,
        'title': 'Report a Crime'
    })