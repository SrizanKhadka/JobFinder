# Generated by Django 5.0.2 on 2024-03-13 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_remove_usermodel_userage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='userAge',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='userCountry',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='userType',
            field=models.CharField(choices=[('Employee', 'EMPLOYEE'), ('Employer', 'EMPLOYER')], default='Employee', max_length=10),
        ),
    ]
