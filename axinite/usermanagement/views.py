# Create your views here.
from axinite.usermanagement.forms import SignUpForm, AdditionalSignUpForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from axinite.utilities.email_messages import REGISTRATION_VERIFICATION_EMAIL
from axinite.utilities.emails import send_registration_email
from axinite.utilities.key import get_verification_key
from axinite.settings import BASE_URL

from axinite.usermanagement.models import UserProfile

def accountcreation(request):
    """
    Settings up user account
    """
    if request.method == "POST":
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            cd = signup_form.cleaned_data
            username = cd['username']
            first_name = cd['first_name']
            last_name = cd['first_name']
            email = cd['first_name']
            password = cd['first_name']
            confirm_password = cd['first_name']
            gender = cd['first_name']
            date_of_birth = cd['first_name']
        else:
            "SignUpForm is Invalid"
            
    else:
        signup_form = SignUpForm()
    return render_to_response("usermanagement/accountsetup_page.html",
                              {'signup_form':signup_form},
                              context_instance=RequestContext(request)
                              )
    

def registration(request):
    """
    Settings up user account
    """
    
    if request.method == "POST":
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            data = signup_form.cleaned_data
            register_user(data)
            return HttpResponseRedirect('/email_sent')
    else:
        signup_form = SignUpForm()
    return render_to_response("usermanagement/registration.html",
                              {'signup_form':signup_form},
                              context_instance=RequestContext(request))

def invalid_key(request):
    return render_to_response("usermanagement/invalid_key.html")

def email_sent(request):
    return render_to_response("usermanagement/email_sent.html")

def profile(request):
    return render_to_response("usermanagement/profile.html")

def verify_registration(request):
    
    key = request.GET.get('key')
    try:
        profile = UserProfile.objects.get(key=key)
    except:
        return HttpResponseRedirect("/invalid_key")
    
    additional_form = AdditionalSignUpForm()
    return render_to_response("usermanagement/registration_confirmation.html",
                              {'additional_form':additional_form,
                               'profile' : profile},
                              context_instance=RequestContext(request))


def register_user(data):
    
    user = User.objects.create_user(data['username'], 
                                    data['confirm_email'], 
                                    data['confirm_password'])
    
    user.save()
    key = get_verification_key()
    profile = user.profile
    profile.key = key
    profile.first_name = data['first_name']
    profile.last_name = data['last_name']
    profile.save()
    
    message = """Hi %s,
    
    You have successfully registered with Axinite.
    
    Please follow the link below to complete your registration:
    
    http://%s/verify/?key=%s
                    
    Regards,
    Axinite Team
    
    """ % (data['first_name'],BASE_URL, key)
    
    send_registration_email(message,
                            'Welcome to Axinite', 
                            data['confirm_email'])                                
    
    