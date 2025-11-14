from django.db import models
from django.utils import timezone
from datetime import date

class Student(models.Model):
    """Student model for storing student information"""
    first_name = models.CharField(max_length=100, verbose_name='نام')
    last_name = models.CharField(max_length=100, verbose_name='نام خانوادگی')
    email = models.EmailField(unique=True, verbose_name='ایمیل')
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='شماره تماس')
    join_date = models.DateField(default=timezone.now, verbose_name='تاریخ عضویت')
    courses_completed = models.TextField(blank=True, verbose_name='دوره‌های گذرانده شده')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'دانشجو'
        verbose_name_plural = 'دانشجویان'
        ordering = ['-join_date']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        """Return full name of student"""
        return f"{self.first_name} {self.last_name}"

    @property
    def membership_duration(self):
        """Calculate membership duration in days"""
        delta = date.today() - self.join_date
        return delta.days

    @property
    def courses_list(self):
        """Return list of courses"""
        if self.courses_completed:
            return [course.strip() for course in self.courses_completed.split(',')]
        return []

    @property
    def courses_count(self):
        """Count number of courses completed"""
        return len(self.courses_list) if self.courses_completed else 0