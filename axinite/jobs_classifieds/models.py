#django imports
from django.db import models
from django.contrib.auth.models import User
#-----------------------------------------------------------------------------
# axinite imports
from axinite.axprofile.models import Country,State,City
#-----------------------------------------------------------------------------

class JobsClassified(models.Model):
    owner = models.ForeignKey(User)
    job = models.BooleanField(default=False)
    summary = models.TextField(null=True,blank=True)
    tags = models.IntegerField(null=True,blank=True)
    job_start = models.DateTimeField()
    job_end = models.DateTimeField()
    country = models.ForeignKey(Country,null=True,blank=True)
    state = models.ForeignKey(State,null=True,blank=True)
    city = models.ForeignKey(City,null=True,blank=True)
    watch_count = models.IntegerField(null=True,blank=True)
    # not sure for unicode statements,will change as per requirement
    def __unicode__(self):
        return self.id
    
#-----------------------------------------------------------------------------    
class JobClassifiedSubscriber(models.Model):
    jobs = models.ForeignKey(JobsClassified)
    subscriber = models.ManyToManyField(User,null=True,blank=True)
    # not sure for unicode statements,will change as per requirement
    def __unicode__(self):
        return self.subscriber
    
#-----------------------------------------------------------------------------
class JobsClassifiedsReplies(models.Model):
    jobs = models.ForeignKey(JobsClassified)
    reply = models.TextField(null=True,blank=True)
    subscriber = models.ManyToManyField(User)
    # not sure for unicode statements,will change as per requirement
    def __unicode__(self):
        return self.subscriber
    