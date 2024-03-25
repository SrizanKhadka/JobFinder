from rest_framework import viewsets
from jobs.api.serializer import JobSerializer,ApplicationSerializer
from jobs.models import JobModel,ApplicationModel
from rest_framework import permissions
from jobs.api.permissons import IsJobCreatorOrEmployer,IsApplicant
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class CreateJobsView(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = JobModel.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsJobCreatorOrEmployer]
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def update(self, request, *args, **kwargs):
        print(f"PRIMARY KEY = {kwargs['pk']}")
        self.permission_classes = [IsJobCreatorOrEmployer]
        response = super().update(request, *args, **kwargs)
        return Response({"data:":response.data, "message":"Job updated Successfully!"})
    
    def destroy(self, request, *args, **kwargs):
        self.permission_classes = [IsJobCreatorOrEmployer]
        super().destroy(request, *args, **kwargs)
        return Response({"details":"Job deleted successfully"})


class CreateApplicationsView(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    queryset = ApplicationModel.objects.all()
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


   
