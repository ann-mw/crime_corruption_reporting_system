from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.homepage, name='home'),
    path('register/', views.register, name='register'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path ('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('report/', views.report_crime, name='report_crime'),
    path('view/', views.view_reports, name='view_reports'),

    # login/logout using Django built-in views
    path('login/', auth_views.LoginView.as_view(template_name='crime_reporting_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
