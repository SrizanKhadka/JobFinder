from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from jobs.api.serializer import JobIndustrySerializer, JobSerializer
from jobs.models import JobModel, JobIndustry
from rest_framework import permissions
from jobs.api.permissons import IsJobCreator, IsEmployer
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status

class CreateJobsView(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = JobModel.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsEmployer]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def update(self, request, *args, **kwargs):
        print(f"PRIMARY KEY = {kwargs['pk']}")
        self.permission_classes = [IsJobCreator]
        response = super().update(request, *args, **kwargs)
        return Response({"data:":response.data, "message":"Job updated Successfully!"})
    
    def destroy(self, request, *args, **kwargs):
        self.permission_classes = [IsJobCreator]
        super().destroy(request, *args, **kwargs)
        return Response({"details":"Job deleted successfully"})


   
