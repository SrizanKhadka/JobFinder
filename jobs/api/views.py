from rest_framework import viewsets
from jobs.api.serializer import JobSerializer
from jobs.models import JobModel
from rest_framework import permissions

class CreateJobsView(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = JobModel.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]