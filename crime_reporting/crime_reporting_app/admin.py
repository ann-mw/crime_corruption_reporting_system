
from django.contrib.auth.models import User

from django.contrib import admin
from .models import CrimeRecord

class CrimeRecordAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_occurred', 'status', 'reporter')
    list_filter = ('status', 'date_occurred')
    search_fields = ('title', 'description')
    readonly_fields = ('reporter', 'title', 'description', 'date_occurred', 'location', 'status')
    actions = None  # Remove bulk actions
    
    def has_add_permission(self, request):
        return False  # Remove add button
    
    def has_change_permission(self, request, obj=None):
        return False  # Remove edit button
    
    def has_delete_permission(self, request, obj=None):
        return False  # Remove delete button

admin.site.register(CrimeRecord, CrimeRecordAdmin)