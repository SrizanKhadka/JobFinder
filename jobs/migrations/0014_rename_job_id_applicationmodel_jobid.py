# Generated by Django 5.0.2 on 2024-03-26 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0013_rename_job_applicationmodel_job_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicationmodel',
            old_name='job_Id',
            new_name='jobId',
        ),
    ]
