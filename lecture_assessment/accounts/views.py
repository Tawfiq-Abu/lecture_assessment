from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms

# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    #here we need to redirect it to the login form
    success_url = reverse_lazy('login')
    #when you create a template for the signup you put it here
    template_name = ''