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
    aboutme = models.CharField(max_length=1024)
    key = models.CharField(max_length=1024)
    key_expires = models.DateTimeField(default=\
                                       datetime.datetime.now() + \
                                       timedelta(days=USER_KEY_EXPIRATION_DAYS))
    profile_photo = models.CharField(max_length=1024)
<<<<<<< HEAD
    gender = models.CharField(max_length=10)
    birthday = models.CharField(max_length=20)
    hometown = models.CharField(max_length=30)
=======
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
    
>>>>>>> dac7375677b37f4d2bf7d5df294655fa4ed6612c
#-------------------------------------------------------------------------------    
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
#-------------------------------------------------------------------------------
class UserEducation(models.Model):
    user = models.ForeignKey(User, unique=False)
    school = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
#-------------------------------------------------------------------------------
class UserWorkHistory(models.Model):
    user = models.ForeignKey(User, unique=False)
    position = models.CharField(max_length=200)
    employer = models.CharField(max_length=200)
    start_date = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
#-------------------------------------------------------------------------------
class UserReligiousViews(models.Model):
    user = models.ForeignKey(User, unique=False)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1024)
#-------------------------------------------------------------------------------
class UserPoliticalViews(models.Model):
    user = models.ForeignKey(User, unique=False)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1024)
#-------------------------------------------------------------------------------
class UserLanguages(models.Model):
    user = models.ForeignKey(User, unique=False)
    language = models.CharField(max_length=100)
#-------------------------------------------------------------------------------
class UserFriends(models.Model):
    user = models.ForeignKey(User, unique=False)
    friend_name = models.CharField(max_length=250)
    friend_id = models.CharField(max_length=200)
    social_site = models.CharField(max_length=200)
#-------------------------------------------------------------------------------
#increase email field length
def email_field_init(self, *args, **kwargs):
  kwargs['max_length'] = kwargs.get('max_length', 200)
  CharField.__init__(self, *args, **kwargs)
EmailField.__init__ = email_field_init
