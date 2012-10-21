#----------------Django Imports---------------------------
from django import forms
from django.forms.widgets import *
from django.forms.models import inlineformset_factory
#-----------------Axinite Imports-------------------------
from axinite.axusers.models import Interest,UserReligiousViews,\
UserPoliticalViews


class AdditionalSignUpForm(forms.Form):
    """
    This describes the additional information when the user is registering
    for the first time.
    """
    def __init__(self, *args, **kwargs):
        super(AdditionalSignUpForm, self).__init__(*args, **kwargs)
        self.fields['political_views'].empty_label = None
        self.fields['religious_views'].empty_label = None

    nationality = forms.CharField(
                                    label="Nationality",max_length=120,\
                                    required=False
                                )
    location = forms.CharField(
                                    label="Current Location",max_length=256,\
                                    required=False
                                )
#    #Employment History
#    company_name = forms.CharField(
#                                    label="Company Name",max_length=256,\
#                                    required=False,widget=forms.TextInput(attrs=\
#                                                           {'class':'input-medium'})
#                                )
#    designation = forms.CharField(
#                                    label="Position",max_length=120,\
#                                    required=False,widget=forms.TextInput(attrs=\
#                                                           {'class':'input-medium'})
#                                )
#    date_of_joining = forms.DateField(label="From",required=True,widget=forms.TextInput(attrs=\
#                                                           {'class':'input-small'}))
#    date_of_leaving = forms.DateField(label="To",required=True,widget=forms.TextInput(attrs=\
#                                                           {'class':'input-small'}))
#    # Education History
#    qualification_level = forms.CharField(
#                                        label="Qualification Level",max_length=256,\
#                                        required=False,widget=forms.TextInput(attrs=\
#                                                           {'class':'input-medium'})
#                                        )
#    university = forms.CharField(
#                                    label="University",max_length=256,\
#                                    required=False,widget=forms.TextInput(attrs=\
#                                                           {'class':'input-medium'})
#                                )
    #course_type = forms.ModelChoiceField(
    #                                    queryset=CourseType.objects.all(),
    #                                    required=False,
    #                                    )
#    branch = forms.CharField(
#                                    label="Branch",max_length=256,\
#                                    required=False,widget=forms.TextInput(attrs=\
#                                                           {'class':'input-small'})
#                                )
#    year_of_passout = forms.CharField(
#                                    max_length=10,required=False,\
#                                    label="Year",widget=forms.TextInput(attrs=\
#                                                           {'class':'input-small'})
#                                    )
    
    #Interest
    interest = forms.ModelMultipleChoiceField(
                        queryset = Interest.objects.all(),                          
                        widget=CheckboxSelectMultiple,
                        required=False,
                        )
    
    political_views = forms.ModelChoiceField(queryset=UserPoliticalViews.objects.all(),\
                                             widget = RadioSelect(),\
                                             required=False,\
                                             )
    religious_views = forms.ModelChoiceField(queryset=UserReligiousViews.objects.all(),\
                                             widget = RadioSelect(),\
                                             required=False,\
                                             )