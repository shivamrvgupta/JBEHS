# Generated by Django 3.1 on 2020-09-03 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20200903_0914'),
        ('teachers', '0002_teachersdetail_photo'),
        ('results', '0002_auto_20200828_1010'),
        ('school', '0002_auto_20200828_0805'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clas',
            new_name='Class',
        ),
    ]
