# Generated by Django 3.1 on 2020-08-28 07:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=150)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('modified_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='TeachersDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('d_o_b', models.DateTimeField(max_length=100)),
                ('mobile_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('address_1', models.CharField(max_length=270)),
                ('address_2', models.CharField(blank=True, max_length=275)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=75)),
                ('zipcode', models.CharField(max_length=10)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('modified_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_code', models.CharField(max_length=10)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('modified_date', models.DateTimeField(default=datetime.datetime.now)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.teachersdetail')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.role')),
            ],
        ),
    ]
