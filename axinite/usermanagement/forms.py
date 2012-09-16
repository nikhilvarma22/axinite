from django import forms
from django.forms.widgets import PasswordInput, Select
from axinite.utilities.model_choices import GENDER_CHOICES
from axinite.utilities.date_widget import CustomDateField

class SignUpForm(forms.Form):
    """
    Primary SignUp Form for user
    """
    username = forms.CharField(label="Username/Email:",max_length=80,\
                                 initial='Username',\
                                 required=True
                                 )
    first_name = forms.CharField(label="First Name:",max_length=80,\
                                 initial='First Name',\
                                 required=True
                                 )
    last_name = forms.CharField(label="Last Name:",max_length=80,\
                                 initial='Last Name',\
                                 required=True
                                 )
    email = forms.EmailField(label="Your Email:",required=True,\
                             initial="abc@def.com",
                             )
    confirm_email = forms.EmailField(label="Re-Enter Email",\
                                     required=True,initial="abc@def.com"
                                     )
    password = forms.CharField(label="New Password:",\
                                widget=forms.PasswordInput(),\
                                initial="123abc",
                                required=True
                                )
    confirm_password = forms.CharField(label="Confirm Password",\
                                       widget=forms.PasswordInput(),\
                                       initial="123abc",
                                       )
    gender = forms.CharField(label="I am", max_length=20,\
                             widget=Select(choices=GENDER_CHOICES),
                             required=True
                             )
    date_of_birth = CustomDateField(label="Birthday",required=True)
    
    def clean_email(self):
        """
        Validating Email Field
        """
        if self.data.get('email') != self.data.get("confirm_email"):
            raise forms.ValidationError("Your emails do not match. Please try again.")
        return self.cleaned_data 
    
    def clean_password(self):
        """
        Validating Email Field
        """
        if self.data.get('password') != self.data.get("confirm_password"):
            raise forms.ValidationError("Your passwords do not match. Please try again.")
        return self.cleaned_data 

class AdditionalSignUpForm(forms.Form):
    """
    Fields for complete registration
    """
    nationality = forms.CharField(label="Nationality",max_length=80,\
                                 initial='Nationality',\
                                 required=True
                                 )