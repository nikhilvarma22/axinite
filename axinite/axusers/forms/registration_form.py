#django imports
import datetime
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

#-------------------------------------------------------------------------------
class RegistrationForm(forms.Form):
    """
    Primary SignUp Form for user
    """
    
    
    GENDER_CHOICES = (
        ('select_sex', 'Select Sex'),
        ('male', 'Male'),
        ('female', 'Female'),
    )

    username = forms.CharField(label="Username/Email:",max_length=80,\
                                 initial='Username',\
                                 required=True,
                                 widget=forms.TextInput(attrs=\
                                                           {'class':'k-textbox'})
                                 )
    first_name = forms.CharField(label="First Name:",max_length=80,\
                                 initial='First Name',\
                                 required=True,
                                 widget=forms.TextInput(attrs=\
                                                           {'class':'k-textbox'})

                                 )
    last_name = forms.CharField(label="Last Name:",max_length=80,\
                                 initial='Last Name',\
                                 required=True,
                                 widget=forms.TextInput(attrs=\
                                                           {'class':'k-textbox'})

                                 )
    email = forms.EmailField(label="Your Email:",required=True,\
                             initial="abc@def.com",
                                 widget=forms.TextInput(attrs=\
                                                           {'class':'k-textbox'})

                             )
    confirm_email = forms.EmailField(label="Re-Enter Email",\
                                     required=True,initial="abc@def.com",
                                 widget=forms.TextInput(attrs=\
                                                           {'class':'k-textbox'})

                                     )
    password = forms.CharField(label="New Password:",\
                                widget=forms.PasswordInput(attrs={'class':
                                                                  'k-textbox'}),\
                                initial="123abc",
                                required=True,
                                )
    confirm_password = forms.CharField(label="Confirm Password",\
                                       widget=forms.PasswordInput(attrs=\
                                                                  {'class':
                                                                  'k-textbox'}),
                                       initial="123abc",

                                       )
    gender =  forms.ChoiceField(label="I am", choices=GENDER_CHOICES,
                             required=True
                             )
    date_of_birth = forms.DateField(label="Date of birth", 
                                    initial=datetime.date.today,
                                    required=True,
                                    widget=forms.TextInput(attrs=\
                                                           {'class':'form_date'}))
    
    #---------------------------------------------------------------------------
    def clean_email(self):
        """
        Validating Email Field
        """
        if self.data.get('email') != self.data.get("confirm_email"):
            raise forms.ValidationError("Your emails do not match. Please try again.")
        
        try:
            User.objects.get(email=self.data.get('email'))
        except ObjectDoesNotExist:
            return self.data.get('email')
        except:
            pass
        raise forms.ValidationError("Email is already registered.")
        
     
    #---------------------------------------------------------------------------
    def clean_password(self):
        """
        Validating Email Field
        """
        if self.data.get('password') != self.data.get("confirm_password"):
            raise forms.ValidationError("Your passwords do not match. Please try again.")
        return self.data.get('password')
    
    #---------------------------------------------------------------------------
    def clean_username(self):
        """
        Validating username
        """
        try:
            user = User.objects.get(username=self.data.get('username'))
        except ObjectDoesNotExist:
            return self.data.get('username')
        except:
            pass
        raise forms.ValidationError("Username is already taken.")
            
#-------------------------------------------------------------------------------