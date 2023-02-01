# Generated by Django 4.1.6 on 2023-02-01 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('mobile_number', models.IntegerField()),
                ('email_address', models.EmailField(default='', max_length=254)),
            ],
        ),
    ]
