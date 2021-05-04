from django.urls import path
from .views import AssessmentView

urlpatterns = [
    path('', AssessmentView.as_view())
]