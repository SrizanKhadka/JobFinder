from rest_framework import serializers
from jobs.models import *
from drf_writable_nested import WritableNestedModelSerializer

<<<<<<< HEAD
class JobSerializer(serializers.ModelSerializer):

    # jobIndustry = JobIndustrySerializer()
    # jobIndustry = serializers.StringRelatedField()

    class Meta:
        model = JobModel
        fields = "__all__"

#using writableNestedModelSerializer.
class JobIndustrySerializer(WritableNestedModelSerializer):
    
    jobIndustry = JobSerializer(many=True,read_only=True)
=======

class JobIndustrySerializer(serializers.ModelSerializer):
>>>>>>> 813aeef8fc55d865ea01ce89879118d6cabd0f7f

    class Meta:
        model = JobIndustry
        fields = "__all__"

<<<<<<< HEAD
    # def create(self, validated_data):
    #     try:
    #         # if there is already an instance in the database with the
    #         # given value (e.g. industryName='Finance'), we simply return this instance
    #         return JobIndustry.objects.get(industryName=validated_data['industryName'])
    #     except ObjectDoesNotExist:
    #         # else, we create a new tag with the given value
    #         return super(JobIndustrySerializer, self).create(validated_data)
    


=======
>>>>>>> 813aeef8fc55d865ea01ce89879118d6cabd0f7f
#with default create method.
class JobSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):

    jobIndustry = JobIndustrySerializer()
    jobCreator = serializers.StringRelatedField()

    class Meta:
        model = JobModel
        fields = "__all__"

    def create(self, validated_data):
        job_industry_data = validated_data.pop('jobIndustry')
        print(f"JOB_INDUSTRY_DATA = {job_industry_data}")
        job_industry, created = JobIndustry.objects.get_or_create(**job_industry_data)
        job = JobModel.objects.create(jobIndustry=job_industry, **validated_data)
        return job
    

class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApplicationModel
        fields = "__all__"

        


 

#using writableNestedModelSerializer.

# class JobSerializer(WritableNestedModelSerializer):

#     jobIndustry = JobIndustrySerializer()
#     # jobIndustry = serializers.StringRelatedField()

#     class Meta:
#         model = JobModel
#         fields = "__all__"