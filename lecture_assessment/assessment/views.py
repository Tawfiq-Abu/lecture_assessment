from django.shortcuts import render
from django.views import generic

# Create your views here.
class AssessmentView(generic.CreateView):
    template = "assessment/assessment_form.html"
    