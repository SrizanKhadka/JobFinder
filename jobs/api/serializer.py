from rest_framework import serializers
from jobs.models import *
from drf_writable_nested import WritableNestedModelSerializer


class JobIndustrySerializer(serializers.ModelSerializer):

    class Meta:
        model = JobIndustry
        fields = "__all__"

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