from rest_framework import viewsets
<<<<<<< HEAD
from jobs.api.serializer import JobIndustrySerializer,JobSerializer
from jobs.models import JobModel, JobIndustry
=======
from jobs.api.serializer import JobSerializer,ApplicationSerializer
from jobs.models import JobModel,ApplicationModel
>>>>>>> 813aeef8fc55d865ea01ce89879118d6cabd0f7f
from rest_framework import permissions
from jobs.api.permissons import IsJobCreatorOrEmployer,IsApplicant
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters



class CreateJobsView(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = JobModel.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsJobCreatorOrEmployer]
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10

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
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('job',)


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def list(self, request, *args, **kwargs):
       response = super().list(request, *args, **kwargs)
       return Response(
           {"data":response.data,"message":"All applications"}
       )
   
