from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """Admin interface for Student model"""
    list_display = ['full_name', 'email', 'phone', 'courses_count', 'membership_duration', 'join_date', 'is_active']
    list_filter = ['is_active', 'join_date']
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    readonly_fields = ['created_at', 'updated_at', 'membership_duration']
    date_hierarchy = 'join_date'
    list_per_page = 20
    
    fieldsets = (
        ('اطلاعات شخصی', {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),
        ('اطلاعات تحصیلی', {
            'fields': ('courses_completed', 'join_date', 'is_active')
        }),
        ('اطلاعات سیستمی', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def membership_duration(self, obj):
        return f"{obj.membership_duration} روز"
    membership_duration.short_description = 'مدت عضویت'
    
    def courses_count(self, obj):
        return obj.courses_count
    courses_count.short_description = 'تعداد دوره‌ها'