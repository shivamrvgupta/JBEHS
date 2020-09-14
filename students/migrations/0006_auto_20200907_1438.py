# Generated by Django 3.1 on 2020-09-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20200905_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='student_code',
        ),
        migrations.AddField(
            model_name='photo',
            name='fullname',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, upload_to='students/%Y/%m/%d/'),
        ),
    ]