# Generated by Django 5.0.2 on 2024-03-25 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_applicationmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicationmodel',
            old_name='jobId',
            new_name='job',
        ),
    ]
