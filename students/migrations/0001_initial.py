# Generated by Django 3.1 on 2020-08-28 07:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=75)),
                ('middle_name', models.CharField(max_length=75)),
                ('last_name', models.CharField(max_length=75)),
                ('student_code', models.CharField(max_length=10)),
                ('dateofbirth', models.DateField()),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('mobile_number', models.CharField(max_length=12)),
                ('address_1', models.CharField(max_length=270)),
                ('address_2', models.CharField(blank=True, max_length=275)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=75)),
                ('zipcode', models.CharField(max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('modified_date', models.DateTimeField(default=datetime.datetime.now)),
                ('std', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.class')),
            ],
        ),
    ]
