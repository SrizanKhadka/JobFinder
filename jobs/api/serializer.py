from rest_framework import serializers
from jobs.models import JobModel, JobIndustry
from drf_writable_nested import WritableNestedModelSerializer
from drf_writable_nested.mixins import UniqueFieldsMixin
from django.core.exceptions import ObjectDoesNotExist

class JobSerializer(serializers.ModelSerializer):

    # jobIndustry = JobIndustrySerializer()
    # jobIndustry = serializers.StringRelatedField()

    class Meta:
        model = JobModel
        fields = "__all__"

#using writableNestedModelSerializer.
class JobIndustrySerializer(WritableNestedModelSerializer):
    
    jobIndustry = JobSerializer(many=True,read_only=True)

    class Meta:
        model = JobIndustry
        fields = "__all__"

    # def create(self, validated_data):
    #     try:
    #         # if there is already an instance in the database with the
    #         # given value (e.g. industryName='Finance'), we simply return this instance
    #         return JobIndustry.objects.get(industryName=validated_data['industryName'])
    #     except ObjectDoesNotExist:
    #         # else, we create a new tag with the given value
    #         return super(JobIndustrySerializer, self).create(validated_data)
    


#with default create method.
# class JobSerializer(serializers.ModelSerializer):

#     jobIndustry = JobIndustrySerializer()
#     # jobIndustry = serializers.StringRelatedField()

#     class Meta:
#         model = JobModel
#         fields = "__all__"

#     def create(self, validated_data):
#         job_industry_data = validated_data.pop('jobIndustry')
#         print(f"JOB_INDUSTRY_DATA = {job_industry_data}")
#         job_industry, created = JobIndustry.objects.get_or_create(**job_industry_data)
#         job = JobModel.objects.create(
#             jobIndustry=job_industry, **validated_data)
#         return job


 