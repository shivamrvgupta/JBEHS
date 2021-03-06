# Generated by Django 3.1 on 2020-08-28 07:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.IntegerField()),
                ('subject_code', models.IntegerField()),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('modified_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.CharField(max_length=10)),
                ('english', models.IntegerField()),
                ('hindi', models.IntegerField()),
                ('marathi', models.IntegerField()),
                ('science', models.IntegerField()),
                ('maths', models.IntegerField()),
                ('social_studies', models.IntegerField()),
                ('it', models.IntegerField()),
                ('total', models.IntegerField(default=0)),
                ('outoff', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('modified_date', models.DateTimeField(default=datetime.datetime.now)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.school')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
        ),
    ]
