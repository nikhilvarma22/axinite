#python imports
import datetime
from datetime import timedelta

#django imports
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField

#axinite imports
from axinite.settings import USER_KEY_EXPIRATION_DAYS
#-------------------------------------------------------------------------------
class UserProfile(models.Model):
    """
    This class extends the django user to create profiles for users
    """
    user = models.ForeignKey(User, unique=True)
    key = models.CharField(max_length=1024)
    key_expires = models.DateTimeField(default=\
                                       datetime.datetime.now() + \
                                       timedelta(days=USER_KEY_EXPIRATION_DAYS)) 
#-------------------------------------------------------------------------------    
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
#-------------------------------------------------------------------------------

#increase email field length
def email_field_init(self, *args, **kwargs):
  kwargs['max_length'] = kwargs.get('max_length', 200)
  CharField.__init__(self, *args, **kwargs)
EmailField.__init__ = email_field_init