
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """Admin interface for Student model"""
    list_display = ['full_name', 'email', 'courses_count', 'membership_duration', 'join_date', 'is_active']
    list_filter = ['is_active', 'join_date']
    search_fields = ['first_name', 'last_name', 'email', 'courses_completed']
    readonly_fields = ['join_date']
    
    fieldsets = (
        ('اطلاعات شخصی', {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),
        ('اطلاعات دوره', {
            'fields': ('courses_completed',)
        }),
        ('اطلاعات عضویت', {
            'fields': ('join_date', 'is_active')
        }),
    )
