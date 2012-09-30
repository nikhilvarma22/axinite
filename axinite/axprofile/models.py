from django.db import models
from django.contrib.auth.models import User


class UserFriends(models.Model):
    user = models.ForeignKey(User, unique=False)
    friend_name = models.CharField(max_length=250)
    friend_id = models.CharField(max_length=200)
    social_site = models.CharField(max_length=200)
    