# Generated by Django 3.1.7 on 2021-03-22 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0005_auto_20210322_1940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='first_name',
            new_name='Firstname',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='last_name',
            new_name='Lastname',
        ),
    ]
