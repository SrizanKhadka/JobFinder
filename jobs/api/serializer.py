from rest_framework import serializers
from jobs.models import JobModel,JobIndustry

class JobIndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobIndustry
        fields = "__all__"

class JobSerializer(serializers.ModelSerializer):
    
    jobIndustry = JobIndustrySerializer()
    #jobIndustry = serializers.StringRelatedField()
    
    class Meta:
        model = JobModel
        fields = "__all__"