''' Create Model for Users'''

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create User model
class User(AbstractUser):
    pass