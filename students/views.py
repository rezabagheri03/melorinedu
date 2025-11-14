from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student
from .forms import StudentRegistrationForm, ContactForm

def home(request):
    """Home page view"""
    total_students = Student.objects.filter(is_active=True).count()
    total_courses = Student.objects.exclude(courses_completed='').count()
    
    context = {
        'total_students': total_students,
        'total_courses': total_courses,
    }
    return render(request, 'home.html', context)

def about(request):
    """About page view"""
    return render(request, 'about.html')

def students_list(request):
    """Students list page with search and sort functionality"""
    students = Student.objects.filter(is_active=True)
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        students = students.filter(
            first_name__icontains=search_query
        ) | students.filter(
            last_name__icontains=search_query
        ) | students.filter(
            email__icontains=search_query
        )
    
    # Sort functionality
    sort_by = request.GET.get('sort', '-join_date')
    if sort_by in ['first_name', '-first_name', 'email', '-email', 'join_date', '-join_date']:
        students = students.order_by(sort_by)
    
    context = {
        'students': students,
        'search_query': search_query,
        'sort_by': sort_by,
    }
    return render(request, 'students.html', context)

def contact(request):
    """Contact page view with form handling"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form (send email, save to database, etc.)
            messages.success(request, 'پیام شما با موفقیت ارسال شد. به زودی با شما تماس خواهیم گرفت.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {'form': form}
    return render(request, 'contact.html', context)

def register(request):
    """Student registration page view"""
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'ثبت نام شما با موفقیت انجام شد! خوش آمدید {student.full_name} عزیز')
            return redirect('students')
        else:
            messages.error(request, 'لطفاً خطاهای فرم را برطرف کنید.')
    else:
        form = StudentRegistrationForm()
    
    context = {'form': form}
    return render(request, 'register.html', context)