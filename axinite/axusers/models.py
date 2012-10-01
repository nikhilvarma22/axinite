#python imports
import datetime
from datetime import timedelta

#django imports
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField

#axinite imports
from axinite.settings import USER_KEY_EXPIRATION_DAYS
from axinite.utilities.model_choices import GENDER_CHOICES
from axinite.axprofile.models import City, State, Country
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
    profile_photo = models.CharField(max_length=1024)
    gender = models.CharField(verbose_name="Gender",max_length=10,
                              choices=GENDER_CHOICES
                              )
    birthdate = models.DateField(null=True,blank=True)
    nationality = models.CharField(max_length=1024,null=True,blank=True)
    resident_city = models.ForeignKey(City,
                                      verbose_name = "City",\
                                      null=True,blank=True,
                                      )
    resident_state = models.ForeignKey(State,\
                                       verbose_name="State",\
                                       null=True,blank=True
                                       )
    resident_country = models.ForeignKey(Country,\
                                         verbose_name="Country",\
                                         null=True,blank=True
                                        )
    is_public = models.BooleanField(default="True")
    
#-------------------------------------------------------------------------------    
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
#-------------------------------------------------------------------------------

#increase email field length
def email_field_init(self, *args, **kwargs):
  kwargs['max_length'] = kwargs.get('max_length', 200)
  CharField.__init__(self, *args, **kwargs)
EmailField.__init__ = email_field_init
