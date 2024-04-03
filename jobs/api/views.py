from rest_framework import viewsets
from jobs.api.serializer import JobIndustrySerializer,JobSerializer
from jobs.models import JobModel, JobIndustry
from rest_framework import permissions

class CreateJobsView(viewsets.ModelViewSet):
    serializer_class = JobIndustrySerializer
    queryset = JobIndustry.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]