
from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    """
    Registration form for new students
    """
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'phone', 'courses_completed']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control neon-input',
                'placeholder': 'نام خود را وارد کنید',
                'required': True
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control neon-input',
                'placeholder': 'نام خانوادگی خود را وارد کنید',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control neon-input',
                'placeholder': 'example@email.com',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control neon-input',
                'placeholder': '09123456789',
                'dir': 'ltr'
            }),
            'courses_completed': forms.Textarea(attrs={
                'class': 'form-control neon-input',
                'placeholder': 'دوره‌های گذرانده شده را با کاما جدا کنید (مثال: پایتون، جنگو، React)',
                'rows': 4
            }),
        }
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'email': 'ایمیل',
            'phone': 'شماره تماس (اختیاری)',
            'courses_completed': 'دوره‌های گذرانده شده',
        }
    
    def clean_email(self):
        """Validate email uniqueness"""
        email = self.cleaned_data.get('email')
        if Student.objects.filter(email=email).exists():
            raise forms.ValidationError('این ایمیل قبلاً ثبت شده است.')
        return email

class ContactForm(forms.Form):
    """
    Contact form for user inquiries
    """
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control neon-input',
            'placeholder': 'نام شما'
        }),
        label='نام'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control neon-input',
            'placeholder': 'ایمیل شما'
        }),
        label='ایمیل'
    )
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control neon-input',
            'placeholder': 'موضوع پیام'
        }),
        label='موضوع'
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control neon-input',
            'placeholder': 'پیام شما',
            'rows': 5
        }),
        label='پیام'
    )
