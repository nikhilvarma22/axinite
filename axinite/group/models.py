# django imports
from django.db import models
from django.contrib.auth.models import User

#axinite imports
#from axinite.axprofile.models import UserFriends

class FriendGroup(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=256,
                            verbose_name="Name"
                            )
    description = models.TextField(blank=True,null=True)
    watch_counter = models.IntegerField(null=True,blank=True)
    
    def __unicode__(self):
        return self.name
    

class GroupFriends(models.Model):
    owner = models.ForeignKey(User,\
                              db_column = "owner",
                              related_name = "group_groupfriends_owner"
                              )
    friend = models.ForeignKey(User)
    group = models.ManyToManyField(FriendGroup)
    
class InvitedFriends(models.Model):
    by = models.ForeignKey(User,\
                           db_column = "by",
                           related_name = "group_invitefriends_by"
                           )
    who = models.ManyToManyField(User,\
                                 null=True,blank=True,\
                                 db_column = "who",
                                 related_name = "group_invitefriends_who"
                                 )
    group = models.ManyToManyField(FriendGroup,null=True,blank=True)
    date = models.DateTimeField(null=True,blank=True)
    
    
    