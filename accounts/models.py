from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add any additional fields you want for user registration (e.g., profile picture, bio, etc.)
    # For example:
    # profile_picture = models.ImageField(upload_to='profile_pics/')
    # bio = models.TextField()

    # No need to define username, password, email fields as they are included in the AbstractUser model
    pass
