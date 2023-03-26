from django.db import models

class Job(models.Model):
    id = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_desc = models.TextField()
