# Generated by Django 3.1.1 on 2020-09-14 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_auto_20200911_0655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='dateofbirth',
        ),
    ]