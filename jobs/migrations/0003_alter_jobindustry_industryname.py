# Generated by Django 5.0.2 on 2024-03-14 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_alter_jobmodel_jobindustry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobindustry',
            name='industryName',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
