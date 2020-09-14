from django.contrib import messages
from django.db import models
from decimal import Decimal
from datetime import datetime
from school.models import School, Class
from students.models import Student
# Create your models here.


class Subject(models.Model):
    subject = models.IntegerField()
    subject_code = models.IntegerField()
    created_date = models.DateTimeField(default=datetime.now)
    modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.subject


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    std = models.ForeignKey(Class, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=10)
    english = models.IntegerField()
    hindi = models.IntegerField()
    marathi = models.IntegerField()
    science = models.IntegerField()
    maths = models.IntegerField()
    social_studies = models.IntegerField()
    it = models.IntegerField()
    total = models.IntegerField(default=0)
    outoff = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=datetime.now)
    modified_date = models.DateTimeField(default=datetime.now)

    def _get_total_marks_of_students_(self):
        total_marks = self.english + self.hindi + self.marathi + \
            self.science + self.maths + self.it + self.social_studies
        print('total marks --- {}'.format(total_marks))
        return total_marks
    total_marks = property(_get_total_marks_of_students_)

    def _percentage_(self):
        percentage = (self.total_marks / self.outoff) * 100
        percentage = Decimal("%.2f" % percentage)
        print('percentange -- {:.2f}'.format(percentage))
        return percentage
    percentage = property(_percentage_)
