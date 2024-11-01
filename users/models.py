from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    website = models.URLField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"