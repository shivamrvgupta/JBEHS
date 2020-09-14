from django import forms
from .models import Result
from django.core import validators


class AddResult(forms.ModelForm):
    class Meta:
        model = Result
        fields = ('student', 'std', 'roll_number', 'english', 'hindi', 'marathi',
                  'science', 'maths', 'social_studies', 'it', 'total', 'outoff')
        widgets = {
            'student': forms.Select(attrs={'class': 'browser-default custom-select'}),
            'std': forms.Select(attrs={'class': 'browser-default custom-select '}),
            'roll_number': forms.TextInput(attrs={'class': 'form-control'}),
            'english': forms.NumberInput(attrs={'class': 'form-control'}),
            'hindi': forms.NumberInput(attrs={'class': 'form-control'}),
            'marathi': forms.NumberInput(attrs={'class': 'form-control'}),
            'science': forms.NumberInput(attrs={'class': 'form-control'}),
            'maths': forms.NumberInput(attrs={'class': 'form-control'}),
            'social_studies': forms.NumberInput(attrs={'class': 'form-control'}),
            'it': forms.NumberInput(attrs={'class': 'form-control'}),
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
            'outoff': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ResultUpdate(forms.ModelForm):
    class Meta:
        model = Result
        fields = ('roll_number', 'english', 'hindi', 'marathi',
                  'science', 'maths', 'social_studies', 'it', 'total', 'outoff')
        widgets = {
            'roll_number': forms.TextInput(attrs={'class': 'form-control'}),
            'english': forms.NumberInput(attrs={'class': 'form-control'}),
            'hindi': forms.NumberInput(attrs={'class': 'form-control'}),
            'marathi': forms.NumberInput(attrs={'class': 'form-control'}),
            'science': forms.NumberInput(attrs={'class': 'form-control'}),
            'maths': forms.NumberInput(attrs={'class': 'form-control'}),
            'social_studies': forms.NumberInput(attrs={'class': 'form-control'}),
            'it': forms.NumberInput(attrs={'class': 'form-control'}),
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
            'outoff': forms.NumberInput(attrs={'class': 'form-control'}),
        }
