from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('report/', views.report_crime, name='report_crime'),
    path('view_reports/', views.view_reports, name='view_reports'),
    path('login/', auth_views.LoginView.as_view(template_name='crime_reporting_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]