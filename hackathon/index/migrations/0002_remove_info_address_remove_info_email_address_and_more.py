# Generated by Django 4.1.6 on 2023-02-01 20:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='address',
        ),
        migrations.RemoveField(
            model_name='info',
            name='email_address',
        ),
        migrations.RemoveField(
            model_name='info',
            name='mobile_number',
        ),
        migrations.RemoveField(
            model_name='info',
            name='name',
        ),
        migrations.AddField(
            model_name='info',
            name='ACT',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='info',
            name='GPA',
            field=models.PositiveIntegerField(default=10, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='info',
            name='SATE',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='info',
            name='SATM',
            field=models.IntegerField(default=0),
        ),
    ]
