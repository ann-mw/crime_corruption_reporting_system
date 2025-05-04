from django.apps import AppConfig

class CrimeReportingAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crime_reporting_app'

    def ready(self):
        import crime_reporting_app.signals
