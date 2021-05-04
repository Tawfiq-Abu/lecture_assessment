from django.db import models

<<<<<<< HEAD
from django.contrib import auth
=======
from django.contrib.auth.models import User
>>>>>>> cae0efcaff03cb342a5b1144f0f16b68d44a16e0

# Create your models here.
class UserAccount(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        return self.username
    

