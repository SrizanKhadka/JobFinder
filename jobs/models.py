from django.db import models
from authentication.models import UserModel

# Create your models here.

JOB_TYPE = [
    ("FULL_TIME", "full_time"),
    ("PART_TIME", "part_time"),
    ("CONTRACT", "contract"),
    ("INTERNSHIP", "internship"),
]

<<<<<<< HEAD
=======
APPLICATION_STATUS = [
    ("IN REVIEW","in review"),
    ("APPROVED","approved"),
    ("DENIED","denied")
]



class JobIndustry(models.Model):
    industryName = models.CharField(max_length=20)


    def __str__(self):
        return self.industryName
>>>>>>> 813aeef8fc55d865ea01ce89879118d6cabd0f7f

class JobModel(models.Model):
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name="jobCreator",null=True)
    jobTitle = models.CharField(max_length=100)
    company = models.CharField(max_length=50)
    jobDescription = models.TextField()
    jobRequirements = models.TextField()
    location = models.CharField(max_length=100)
<<<<<<< HEAD
    jobType = models.CharField(max_length=20, choices=JOB_TYPE, default="full_time")
    benefits = models.TextField()
    salary = models.CharField(max_length=100, blank=True, null=True)
=======
    jobIndustry = models.ForeignKey(JobIndustry,on_delete=models.CASCADE,related_name="jobIndustry")
    jobType = models.CharField(max_length=20,choices=JOB_TYPE,default="full_time")
    benefits = models.TextField()
    salary = models.CharField(max_length=100, blank=True, null=True) 
>>>>>>> 813aeef8fc55d865ea01ce89879118d6cabd0f7f
    applicationInstructions = models.TextField()
    contactInformation = models.TextField()
    publishedDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    expirationDate = models.DateTimeField()

    def __str__(self):
        return f"{self.jobTitle} - {self.company}"


<<<<<<< HEAD
class JobIndustry(models.Model):
    industryName = models.CharField(max_length=20)
    jobs = models.ForeignKey(JobModel, on_delete=models.CASCADE, related_name="jobIndustry",default=None)

    def __str__(self):
        return self.industryName
=======

class ApplicationModel(models.Model):
    job = models.ForeignKey(JobModel,on_delete=models.CASCADE,related_name="job_application",null=True)
    application = models.TextField()
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name="applicant",null=True)
    status = models.CharField(max_length=20,choices=APPLICATION_STATUS,default="in review")

    def __str__(self):
        return self.job.jobTitle

    
    
>>>>>>> 813aeef8fc55d865ea01ce89879118d6cabd0f7f
