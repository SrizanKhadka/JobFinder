from django.db import models

# Create your models here.

JOB_TYPE = [
    ("FULL_TIME", "full_time"),
    ("PART_TIME", "part_time"),
    ("CONTRACT", "contract"),
    ("INTERNSHIP", "internship"),
]


class JobModel(models.Model):
    jobTitle = models.CharField(max_length=100)
    company = models.CharField(max_length=50)
    jobDescription = models.TextField()
    jobRequirements = models.TextField()
    location = models.CharField(max_length=100)
    jobType = models.CharField(max_length=20, choices=JOB_TYPE, default="full_time")
    benefits = models.TextField()
    salary = models.CharField(max_length=100, blank=True, null=True)
    applicationInstructions = models.TextField()
    contactInformation = models.TextField()
    publishedDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    expirationDate = models.DateTimeField()

    def __str__(self):
        return f"{self.jobTitle} - {self.company}"


class JobIndustry(models.Model):
    industryName = models.CharField(max_length=20)
    jobs = models.ForeignKey(JobModel, on_delete=models.CASCADE, related_name="jobIndustry",default=None)

    def __str__(self):
        return self.industryName
