#----------------Django Imports---------------------------
from django import forms
from django.forms.widgets import *
#-----------------Axinite Imports-------------------------
from axinite.axusers.models import Interest


class AdditionalSignUpform(forms.Form):
    """
    This describes the additional information when the user is registering
    for the first time.
    """
    
    nationality = forms.CharField(
                                    label="Nationality",max_length=120,\
                                    required=False
                                )
    location = forms.CharField(
                                    label="Current Location",max_length=256,\
                                    required=False
                                )
    #Employment History
    company_name = forms.CharField(
                                    label="Company Name",max_length=256,\
                                    required=False
                                )
    designation = forms.CharField(
                                    label="Position",max_length=120,\
                                    required=False
                                )
    date_of_joining = forms.DateField(label="From",null=True,blank=True)
    date_of_leaving = forms.DateField(label="To",null=True,blank=True)
    # Education History
    qualification_level = forms.CharField(
                                        label="Qualification Level",max_length=256,\
                                        required=False
                                        )
    university = forms.CharField(
                                    label="University",max_length=256,\
                                    required=False
                                )
    #course_type = forms.ModelChoiceField(
    #                                    queryset=CourseType.objects.all(),
    #                                    required=False,
    #                                    )
    branch = forms.CharField(
                                    label="Branch",max_length=256,\
                                    required=False
                                )
    year_of_passout = forms.CharField(
                                    max_length=10,required=False,\
                                    label="Year"
                                    )
    
    #Interest
    interest = forms.ModelMultipleChoiceField(
                        queryset = Interest.objects.all(),                          
                        widget=CheckboxSelectMultiple,
                        required=False,
                        initial = "Interest"
                        )