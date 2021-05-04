from django.shortcuts import render
from django.views import generic


from .models import AssessmentResponse
# Create your views here.
class AssessmentView(generic.CreateView):
    model = AssessmentResponse
    fields = '__all__'
    template_name = "assessment/assessment_form.html"
    