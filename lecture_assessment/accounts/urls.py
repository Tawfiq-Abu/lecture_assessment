from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views 

app_name = 'accounts'

urlpatterns = [
    #create a template for the login view
    path('login/',auth_views.LoginView.as_view(template_name=''),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('signup/',views.SignUp.as_view(),name='signup')
]
