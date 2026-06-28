from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    preferred_currency = models.CharField(
        max_length = 10,
        default="CAD"
    )

    language = models.CharField(
        max_length=20,
        default="en"
    )

    timezone = models.CharField(
        max_length = 50,
        default="America/Toronto"
    )

    def __str__(self):
        return self.username