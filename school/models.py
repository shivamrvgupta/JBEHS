from datetime import datetime
from django.db import models
from teachers.models import Teacher
# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=150)
    school_code = models.CharField(max_length=10)
    address_1 = models.CharField(max_length=270)
    address_2 = models.CharField(max_length=275, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=75)
    zipcode = models.CharField(max_length=10)
    created_date = models.DateTimeField(default=datetime.now)
    modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class Class(models.Model):
    std = models.CharField(max_length=10)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.std
