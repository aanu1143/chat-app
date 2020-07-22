from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class CustomUser(AbstractUser):
    status = models.CharField(max_length=50, null=True)
    
    def get_absolute_url(self):
        return reverse('profile_detail',args=[str(self.id)])
