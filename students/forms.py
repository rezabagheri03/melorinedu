from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    """Form for student registration"""
    
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'phone', 'courses_completed']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام خود را وارد کنید',
                'dir': 'rtl'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام خانوادگی خود را وارد کنید',
                'dir': 'rtl'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@email.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '09123456789 (اختیاری)',
                'dir': 'rtl'
            }),
            'courses_completed': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'نام دوره‌های گذرانده شده را با کاما جدا کنید\nمثال: پایتون پیشرفته, جنگو, ری‌اکت',
                'dir': 'rtl'
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Student.objects.filter(email=email).exists():
            raise forms.ValidationError('این ایمیل قبلاً ثبت شده است.')
        return email

class ContactForm(forms.Form):
    """Contact form for user inquiries"""
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام کامل',
            'dir': 'rtl'
        }),
        label='نام'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'example@email.com'
        }),
        label='ایمیل'
    )
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'موضوع پیام',
            'dir': 'rtl'
        }),
        label='موضوع'
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'پیام خود را بنویسید...',
            'dir': 'rtl'
        }),
        label='پیام'
    )