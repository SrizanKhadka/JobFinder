# Generated by Django 5.0.2 on 2024-03-14 11:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_alter_jobmodel_jobindustry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobmodel',
            name='jobIndustry',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='jobModel', to='jobs.jobindustry'),
        ),
    ]
