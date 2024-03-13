from django.contrib import admin
from jobs.models import JobModel, JobIndustry

# Register your models here.

admin.site.register(JobModel)
admin.site.register(JobIndustry)
