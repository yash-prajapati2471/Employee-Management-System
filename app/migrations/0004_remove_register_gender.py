# Generated by Django 5.1.2 on 2025-01-21 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_register_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='gender',
        ),
    ]
