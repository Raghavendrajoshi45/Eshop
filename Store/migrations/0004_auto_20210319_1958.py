# Generated by Django 3.1.7 on 2021-03-19 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('phone', models.ImageField(max_length=20, upload_to='')),
                ('password', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
