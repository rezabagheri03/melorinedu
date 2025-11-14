from django.contrib import admin
from django.urls import path, include
from students import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('students/', views.students_list, name='students'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
]