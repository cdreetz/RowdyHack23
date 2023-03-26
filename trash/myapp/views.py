from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Job, Course
from .serializers import JobSerializer, CourseSerializer

class JobList(generics.ListCreateAPIView):
    """
    API endpoint that allows jobs to be listed
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class JobDetail(generic.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows old jobs to be destroyed
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_permissions(self):
        if self.request.method =='DELETE':
            return [permissions.IsAdminUser()]
        else:
            return [permissions.IsAuthenticatedOrReadOnly()]

class CourseList(generics.ListCreateAPIView):
    queryset: Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.request.method =='DELETE':
            return [permissions.IsAdminUser()]
        else:
            return [permissions.IsAuthenticatedOrReadOnly()]
        

@api_view(['GET'])
def course_list(request):
    courses = Course.objects.all()

    # perform calculations on the data
    

