from django.db import models

# Create your models here.

class AssessmentResponse(models.Model):
    student_class = models.CharField(max_length=50)
    facilitator = models.CharField(max_length=75)
    course = models.CharField(max_length=50)
    