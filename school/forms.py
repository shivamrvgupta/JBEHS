from django import forms
from .models import School
from django.core import validators


class SchoolRegistration(forms.ModelForm):
    class Meta:
        model = School
        fields = ('name', 'school_code', 'address_1',
                  'address_2', 'city', 'state', 'zipcode')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'school_code': forms.TextInput(attrs={'class': 'form-control'}),
            'address_1': forms.TextInput(attrs={'class': 'form-control'}),
            'address_2': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),

        }


class SchoolUpdate(forms.ModelForm):
    class Meta:
        model = School
        fields = ('name', 'school_code', 'address_1',
                  'address_2', 'city', 'state', 'zipcode')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'school_code': forms.TextInput(attrs={'class': 'form-control'}),
            'address_1': forms.TextInput(attrs={'class': 'form-control'}),
            'address_2': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),
        }
