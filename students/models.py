from django.db import models
from datetime import datetime
from school.models import Class
# Create your models here.


class Student(models.Model):
    std = models.ForeignKey(Class, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=75)
    middle_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    student_code = models.CharField(max_length=10)
    age = models.IntegerField()
    email = models.EmailField()
    mobile_number = models.CharField(max_length=12)
    address_1 = models.CharField(max_length=270)
    address_2 = models.CharField(max_length=275, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=75)
    zipcode = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=datetime.now)
    modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.first_name


class StudentDetail(models.Model):
    student_code = models.CharField(max_length=10, default=None)
    mothers_name = models.CharField(
        max_length=275, verbose_name='Mothers_name')
    mothers_occupation = models.CharField(max_length=100, default=None)
    fathers_name = models.CharField(max_length=275)
    fathers_occupation = models.CharField(max_length=100, default=None)
    student_aadhar_number = models.CharField(max_length=12)
    Annual_Income = [
        ('0-9999', '0-9999'),
        ('10000-50000', '10000-50000'),
        ('50000-99999', '50000-99999'),
        ('100000-500000', '100000-500000'),
        ('500000-1000000', '500000-1000000'),
    ]
    annual_income = models.CharField(
        choices=Annual_Income, default="---Annual Income---", max_length=15)
    authorized_by = models.CharField(
        max_length=275, default=None)
    created_date = models.DateTimeField(default=datetime.now)
    modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.student_code


class Photo(models.Model):
    fullname = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='students/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.fullname
