# Generated by Django 5.0.2 on 2024-03-26 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0016_jobmodel_applications'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobmodel',
            name='applications',
        ),
    ]
