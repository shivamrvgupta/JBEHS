from django.db import models
from datetime import datetime
# Create your models here.


class Role(models.Model):
    role = models.CharField(max_length=150)
    created_date = models.DateTimeField(default=datetime.now)
    modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.role


class TeachersDetail(models.Model):
    photo = models.ImageField(upload_to='media/teacher/%Y/%m/%d/', blank=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    d_o_b = models.DateTimeField(max_length=100)
    mobile_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    address_1 = models.CharField(max_length=270)
    address_2 = models.CharField(max_length=275, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=75)
    zipcode = models.CharField(max_length=10)
    created_date = models.DateTimeField(default=datetime.now)
    modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.first_name


class Teacher(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    name = models.ForeignKey(TeachersDetail, on_delete=models.CASCADE)
    teacher_code = models.CharField(max_length=10)
    created_date = models.DateTimeField(default=datetime.now)
    modified_date = models.DateTimeField(default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name.first_name
