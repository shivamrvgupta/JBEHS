# Generated by Django 3.1 on 2020-09-03 09:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media/students/%Y/%m/%d/'),
        ),
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mothers_name', models.CharField(max_length=275, verbose_name='Mothers_name')),
                ('mothers_signature', models.ImageField(upload_to='media/signature/%Y/%m/%d/')),
                ('fathers_name', models.CharField(max_length=275)),
                ('occupation', models.CharField(max_length=100)),
                ('fathers_signature', models.ImageField(upload_to='media/signature/%Y/%m/%d/')),
                ('student_aadhar_number', models.CharField(max_length=12)),
                ('annual_income', models.CharField(choices=[('0-9999', '0-9999'), ('10000-50000', '10000-50000'), ('50000-99999', '50000-99999'), ('100000-500000', '100000-500000'), ('500000-1000000', '500000-1000000')], default='---Annual Income---', max_length=15)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('modified_date', models.DateTimeField(default=datetime.datetime.now)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
        ),
    ]