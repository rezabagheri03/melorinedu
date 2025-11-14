from django.core.management.base import BaseCommand
from students.models import Student
from datetime import date, timedelta
import random

class Command(BaseCommand):
    help = 'Populate database with sample student data'

    def handle(self, *args, **kwargs):
        # Clear existing students
        Student.objects.all().delete()
        
        # Sample Persian names
        first_names = [
            'محمدرضا', 'علی', 'فاطمه', 'زهرا', 'حسین', 'مهدی', 'سارا', 'مریم',
            'رضا', 'امیر', 'نیلوفر', 'محمد', 'سید', 'پریسا', 'آرمین'
        ]
        last_names = [
            'رضایی', 'محمدی', 'احمدی', 'حسینی', 'علیزاده', 'کریمی', 'نوری', 'موسوی',
            'صادقی', 'جعفری', 'قاسمی', 'فرخی', 'باقری', 'نظری', 'سلیمی'
        ]
        
        courses = [
            'پایتون مقدماتی',
            'جنگو پیشرفته',
            'ری‌اکت و Node.js',
            'طراحی وبسایت با HTML & CSS',
            'جاواسکریپت جامع',
            'مبانی پایگاه داده',
            'هوش مصنوعی و یادگیری ماشین',
            'امنیت سایبری',
            'DevOps و مدیریت سرور',
            'توسعه موبایل',
            'API و RESTful',
            'Git و GitHub'
        ]
        
        students_data = []
        for i in range(15):
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            email = f"{first_name.lower()}.{last_name.lower()}{i}@email.com"
            phone = f"09{random.randint(100000000, 999999999)}"
            
            # Random join date in last 365 days
            days_ago = random.randint(1, 365)
            join_date = date.today() - timedelta(days=days_ago)
            
            # Random courses (1-5 courses)
            num_courses = random.randint(1, 5)
            student_courses = random.sample(courses, num_courses)
            courses_str = ', '.join(student_courses)
            
            student = Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                join_date=join_date,
                courses_completed=courses_str,
                is_active=True
            )
            students_data.append(student)
            
        self.stdout.write(self.style.SUCCESS(f'Successfully created {len(students_data)} students'))
        
        # Display created students
        for student in students_data:
            self.stdout.write(f'  - {student.full_name} ({student.email}) - {student.courses_count} courses')