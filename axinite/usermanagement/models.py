from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)

    key = models.CharField(max_length=1024)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])