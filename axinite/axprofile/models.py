from django.db import models
from django.contrib.auth.models import User

#axinite imports
from axinite.utilities.model_choices import GENDER_CHOICES
#-------------------------------------------------------------------------------

class Country(models.Model):
    """
    List of all the countries.Later on i will add fixtures in this.
    """
    name = models.CharField(verbose_name = "Country",
                            max_length = 1024,
                            null = True, blank=True,
                            )
    
    def __unicode__(self):
        return self.name
#-------------------------------------------------------------------------------
    
class State(models.Model):
    """
    same as that of countries.fixtures will be added.
    """
    name = models.CharField(verbose_name = "State",
                            max_length = 1024,
                            )
    country = models.ForeignKey(Country)
    
    def __unicode__(self):
        return self.name
#-------------------------------------------------------------------------------

class City(models.Model):
    """
    Same as that of countries and states.fixtures will be added.
    """
    
    name = models.CharField(verbose_name = "City",
                            max_length = 1024,
                            )
    country = models.ForeignKey(Country)
    state = models.ForeignKey(State)
    
    def __unicode__(self):
        return self.name

#-------------------------------------------------------------------------------

class UserFriends(models.Model):
    user = models.ForeignKey(User, unique=False)
    friend_name = models.CharField(max_length=250)
    friend_id = models.CharField(max_length=200)
    social_site = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.friend_name
#-------------------------------------------------------------------------------

class EmploymentHistory(models.Model):
    """
    This class describes the employment details of the employee.
    
    """
    user = models.ForeignKey(User)
    company_name = models.CharField(verbose_name ="Name",max_length=256)
    date_of_joining = models.DateField()
    date_of_leaving = models.DateField()
    position = models.CharField(max_length =256,
                                verbose_name="Designation",\
                                null=True,blank=True,
                                )
    
    def __unicode__(self):
        employmenthistory_obj = "%s,%s" %(self.user,self.position)
        return employmenthistory_obj
    
#-------------------------------------------------------------------------------

class CourseType(models.Model):
    name = models.CharField(max_length=1024)
    
    def __unicode__(self):
        return self.name
        
#-------------------------------------------------------------------------------
        
class EducationHistory(models.Model):
    """
    This class describes the education details of the person/employee.
    course type will tell whether the course is full time, part time etc,
    branch will be specialization, qualification level will be whether 
    the user is a graduate or 10+2 etc.
    """
    user = models.ForeignKey(User)
    qualification_level = models.CharField(max_length=40,
                                           null=True,blank=True,\
                                           )
    institute_name = models.CharField(max_length=1024,\
                                      verbose_name="Institute Name",\
                                      )
    course_type = models.ForeignKey(CourseType,\
                                    verbose_name = "Type of Institute"
                                    )
    branch = models.CharField(max_length=256,\
                              verbose_name="Education Specialization",\
                              null=True,blank=True
                              )
    year_of_passout = models.CharField(verbose_name = "Year of Passout",
                                       max_length=10,
                                       blank=True,null=True
                                       )
    
    
    def __unicode__(self):
        return self.qualification_level
    
#-------------------------------------------------------------------------------
