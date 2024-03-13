from django.db import models

# Create your models here.

JOB_TYPE = [
    ("FULL_TIME","full_time"),
    ("PART_TIME","part_time"),
    ("CONTRACT","contract"),
    ("INTERNSHIP","internship")
]

class JobIndustry(models.Model):
    industryName = models.CharField(max_length=20)

    def __str__(self):
        return self.industryName

class JobModel(models.Model):
    jobTitle = models.CharField(max_length=100)
    company = models.CharField(max_length=50)
    jobDescription = models.TextField()
    jobRequirements = models.TextField()
    location = models.CharField(max_length=100)
    jobIndustry = models.ForeignKey(JobIndustry,on_delete=models.CASCADE)
    jobType = models.CharField(max_length=20,choices=JOB_TYPE,default="full_time")
    benefits = models.TextField()
    salary = models.CharField(max_length=100, blank=True, null=True)  # Optional field for salary
    applicationInstructions = models.TextField()
    contactInformation = models.TextField()
    publishedDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    expirationDate = models.DateTimeField()
    filter_location = models.CharField(max_length=100, blank=True, null=True)
    filter_industry = models.ForeignKey(JobIndustry, on_delete=models.CASCADE, related_name='jobs_filtered', blank=True, null=True)
    filter_job_type = models.CharField(max_length=20, choices=JOB_TYPE, default="FULL_TIME", blank=True, null=True)

    def __str__(self):
        return f"{self.jobTitle} - {self.company}"

    
