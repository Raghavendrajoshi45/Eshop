# Generated by Django 3.1.7 on 2021-03-22 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0007_auto_20210322_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
    ]
