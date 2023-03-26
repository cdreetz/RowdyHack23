from rest_framework import serializers
from .models import Job, Course

class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job 
        fields = ['id', 'role', 'company', 'description']


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course 
        fields = ['course_name', 'course_desc']