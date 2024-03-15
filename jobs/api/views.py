from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from jobs.api.serializer import JobIndustrySerializer, JobSerializer
from jobs.models import JobModel, JobIndustry
from rest_framework import permissions
from jobs.api.permissons import IsJobCreatorOnly, IsEmployer

class CreateJobsView(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = JobModel.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsEmployer]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
