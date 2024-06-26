# Generated by Django 5.0.2 on 2024-03-13 12:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobIndustry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industryName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='JobModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobTitle', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=50)),
                ('jobDescription', models.TextField()),
                ('jobRequirements', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('jobType', models.CharField(choices=[('FULL_TIME', 'full_time'), ('PART_TIME', 'part_time'), ('CONTRACT', 'contract'), ('INTERNSHIP', 'internship')], default='full_time', max_length=20)),
                ('benefits', models.TextField()),
                ('salary', models.CharField(blank=True, max_length=100, null=True)),
                ('applicationInstructions', models.TextField()),
                ('contactInformation', models.TextField()),
                ('publishedDate', models.DateTimeField(auto_now_add=True)),
                ('updatedDate', models.DateTimeField(auto_now=True)),
                ('expirationDate', models.DateTimeField()),
                ('filter_location', models.CharField(blank=True, max_length=100, null=True)),
                ('filter_job_type', models.CharField(blank=True, choices=[('FULL_TIME', 'full_time'), ('PART_TIME', 'part_time'), ('CONTRACT', 'contract'), ('INTERNSHIP', 'internship')], default='FULL_TIME', max_length=20, null=True)),
                ('filter_industry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs_filtered', to='jobs.jobindustry')),
                ('jobIndustry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.jobindustry')),
            ],
        ),
    ]
