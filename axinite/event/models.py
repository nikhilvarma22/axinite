#-----------------Django imports ---------------#
from django.db import models
from django.contrib.auth.models import User


class Share(models.Model):
    """
    This class describes the category of events like whether it is public,\
    private etc.
    """
    
    name = models.CharField(max_length=80, null=True,blank=True)
    
    def __unicode__(self):
        return self.name


class Event(models.Model):
    """ 
    This class describes the events.
    topic = what event is all about / title of event
    likes , dislikes = likes and dislikes for event
    ratings = no. of votes that that event
    """
    topic = models.CharField(max_length=80,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    location = models.CharField(max_length=80, null=True,blank=True)
    share_with = models.ForeignKey(Share,null=True,blank=True)
    tags = models.CharField(max_length=80,null=True,blank=True)
    likes = models.IntegerField(null=True,blank=True)
    dislikes = models.IntegerField(null=True,blank=True)
    ratings = models.IntegerField(null=True,blank=True)
    watch_count = models.IntegerField(null=True,blank=True)
    
    def __unicode__(self):
        return self.topic + self.location


class Participant(models.Model):
    """
    This class describes the users who will be participating 
    in the event.
    """
    
    event = models.ForeignKey(Event,null=True,blank=True)
    participants = models.ManyToManyField(User, related_name='participant',\
                                         verbose_name='Participant',\
                                         null=True, blank=True
                                         )
    
    def __unicode__(self):
        return self.participants


class Organizer(models.Model):
    """
    This class describes the users who organizes the event.
    """
    
    event = models.ForeignKey(Event,\
                             null=True,blank=True,\
                             help_text="who organizes the event",\
                             )
    organizers = models.ManyToManyField(User, related_name='organizers',\
                                        verbose_name="Organizers",\
                                        null=True, blank=True
                                        )
    
    def __unicode__(self):
        return self.organizers
    
    
class Subscriber(models.Model):
    """
    This class describes the users who subscribes the event.
    subscribed = At what day and time it was subscribed
    """
    event = models.ForeignKey(Event,null=True,blank=True)
    subscribers = models.ManyToManyField(User, related_name='subscriptions',\
                                         verbose_name='Subscribers',\
                                         null=True, blank=True
                                         )
    subscribed = models.DateTimeField(null=True,blank=True)
    
    def __unicode__(self):
        return self.subscribers

class ReportAbuse(models.Model):
    """
    This class is for handling the Abuses
    abuse_reason = reason for abuse
    reported_by = which user is basically abusing.
    reported = at what date & time the user abused  
    """
    event = models.ForeignKey(Event)
    abuse_reason = models.TextField(null=True,blank=True)
    reported_by = models.ForeignKey(User)
    reported = models.DateTimeField(null=True,blank=True)
    
    def __unicode__(self):
        return self.reported
        

class Comment(models.Model):
    """
    This class describes the comments for its respective event.
    title = comment title
    reviews = reviews describe by the user for the particular event.
    status = Whether to show the comment of not
    ratings = Vote for this comment
    datetime = When it was written
    """
    
    title = models.CharField(max_length=1024,null=True, blank=True)
    event = models.ForeignKey(Event)
    commentor = models.ForeignKey(User)
    reviews = models.TextField(null=True,blank=True)
    datetime = models.DateTimeField(null=True,blank=True)
    ratings = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default=True)
    
    def __unicode__(self):
        comment_obj = "%s, %s" % (self.event, self.reviews)
        return comment_obj 
    

class SpamComment(models.Model):
    """
    """
    event = models.ForeignKey(Event,null=True,blank=True)
    reported = models.DateTimeField(null=True,blank=True)
    
    def __unicode__(self):
        spamcomment = "%s, %s" %(self.event, self.reported)
        return spamcomment
    
