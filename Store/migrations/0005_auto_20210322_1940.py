# Generated by Django 3.1.7 on 2021-03-22 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0004_auto_20210319_1958'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='Firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='Lastname',
            new_name='last_name',
        ),
    ]
