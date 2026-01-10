from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Admin interface for Booking model"""
    
    list_display = ['name', 'phone', 'date', 'level', 'class_time', 'created_at']
    list_filter = ['level', 'date', 'created_at']
    search_fields = ['name', 'phone']
    date_hierarchy = 'date'
    ordering = ['-date', 'class_time']
    
    fieldsets = (
        ('Student Information', {
            'fields': ('name', 'phone')
        }),
        ('Class Details', {
            'fields': ('date', 'level', 'class_time')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at', 'class_time']
    
    def get_readonly_fields(self, request, obj=None):
        """Make class_time readonly as it's auto-set based on level"""
        if obj:  # Editing an existing object
            return self.readonly_fields + ['level']
        return self.readonly_fields
