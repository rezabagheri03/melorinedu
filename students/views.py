
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Student
from .forms import StudentRegistrationForm, ContactForm

def home(request):
    """Home page view"""
    students_count = Student.objects.filter(is_active=True).count()
    total_courses = sum(student.courses_count for student in Student.objects.all())
    
    context = {
        'students_count': students_count,
        'total_courses': total_courses,
        'active_page': 'home'
    }
    return render(request, 'home.html', context)

def about(request):
    """About page view"""
    context = {
        'active_page': 'about'
    }
    return render(request, 'about.html', context)

def students_list(request):
    """Students list page with search functionality"""
    search_query = request.GET.get('search', '')
    
    students = Student.objects.filter(is_active=True)
    
    if search_query:
        students = students.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(courses_completed__icontains=search_query)
        )
    
    context = {
        'students': students,
        'search_query': search_query,
        'active_page': 'students'
    }
    return render(request, 'students.html', context)

def contact(request):
    """Contact page view with form handling"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # In production, you would send email here
            messages.success(request, 'پیام شما با موفقیت ارسال شد. به زودی با شما تماس خواهیم گرفت.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'active_page': 'contact'
    }
    return render(request, 'contact.html', context)

def register(request):
    """Student registration page view"""
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'ثبت نام با موفقیت انجام شد! خوش آمدید {student.full_name}')
            return redirect('students')
    else:
        form = StudentRegistrationForm()
    
    context = {
        'form': form,
        'active_page': 'register'
    }
    return render(request, 'register.html', context)
