from django.urls import include,path
from rest_framework import routers
from .views import JobList, JobDetail, CourseList, CourseDetail

router = routers.DefaultRouter()
router.register(r'jobs', views.JobViewSet)
router.register(r'courses', views.CourseViewSet)

# wire up our API using automatic URL routing
# additionally we include login URLs for the browsable API
urlpatters = [
    path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]