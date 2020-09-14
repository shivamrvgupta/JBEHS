from django import forms
from .models import Student, StudentDetail, Photo
from django.core import validators
from datetime import datetime


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'middle_name',
                  'last_name', 'student_code', 'std', 'age', 'email', 'mobile_number', 'address_1', 'address_2', 'city', 'state', 'zipcode')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'student_code': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'std': forms.Select(attrs={'class': 'browser-default custom-select'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address_1': forms.TextInput(attrs={'class': 'form-control'}),
            'address_2': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class StudentUpdate(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'middle_name',
                  'last_name', 'student_code', 'std', 'age', 'mobile_number', 'address_1', 'address_2', 'city', 'state', 'zipcode')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'std': forms.Select(attrs={'class': 'browser-default custom-select'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'student_code': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address_1': forms.TextInput(attrs={'class': 'form-control'}),
            'address_2': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class StudentDetailsForm(forms.ModelForm):
    class Meta:
        model = StudentDetail
        fields = ('student_code', 'mothers_name', 'mothers_occupation',
                  'fathers_name', 'fathers_occupation', 'student_aadhar_number', 'annual_income', 'authorized_by')
        widgets = {
            'student_code': forms.TextInput(attrs={'class': 'form-control'}),
            'mothers_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mothers_occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'fathers_name': forms.TextInput(attrs={'class': 'form-control'}),
            'fathers_occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'student_aadhar_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'fathers_name': forms.TextInput(attrs={'class': 'form-control'}),
            'annual_income': forms.Select(attrs={'class': 'browser-default custom-select'}),
            'authorized_by': forms.TextInput(attrs={'class': 'form-control'}),
        }


class StudentPhoto(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(attrs={'class': 'custom-file-input', 'id': 'inputGroupFile01'}),
        }
