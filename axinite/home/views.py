#django imports
from django.core.mail import EmailMessage
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login

#axinite imports
from axinite.settings import BASE_URL
from axinite.axusers.views import register_user
from axinite.axusers.forms.registration_form import RegistrationForm
from axinite.axusers.forms.login_form import LoginForm
#-------------------------------------------------------------------------------
def home(request):
    """
    This view renders the home page and handles all form processing on the home 
    page.
    """
    
    if request.method == 'POST':
        if request.POST['formname'] == 'registration':
            form_registration = RegistrationForm(request.POST)
            form_login = LoginForm()
            if form_registration.is_valid():
                userdata = form_registration.cleaned_data
                user = register_user(userdata)
                if user:
                    address = user.email
                    redirect_to = '/registration_confirmation?email=%s' % \
                    address
                    
                    subject=''
                    message = """Hi %s,
                    
                     You have successfully registered with Axinite.
    
                     Please follow the link below to complete your registration:
                        
                     http://%s/verify_registration/?key=%s&username=%s
                                        
                     Regards,
                     Axinite Team
                     
                    """ % (user.first_name, BASE_URL, user.profile.key, 
                           user.username)
                    email = EmailMessage(subject, message, to=[address])
                    email.send()
                else:
                    redirect_to = '/registration_failure'
                return HttpResponseRedirect(redirect_to)
        if request.POST['formname'] == 'login':
            form_login = LoginForm(request.POST)
            form_registration = RegistrationForm()
            if form_login.is_valid():
                data = form_login.cleaned_data
                user = authenticate(username=data['username'], 
                                    password=data['password'])
                login(request, user)
                return HttpResponseRedirect('/axprofile')
    else:
        form_registration = RegistrationForm()
        form_login = LoginForm()
    
    return render_to_response("home/home.html",
                              {'form_registration':form_registration,
                               'form_login' : form_login},
                              context_instance=RequestContext(request))
#-------------------------------------------------------------------------------
def get_user_avatar(backend, details, response, social_user, uid,\
                    user, *args, **kwargs):
    url = None
    if backend.__class__ == FacebookBackend:
        url = "http://graph.facebook.com/%s/picture?type=large" % response['id']
 
    elif backend.__class__ == TwitterBackend:
        url = response.get('profile_image_url', '').replace('_normal', '')
 
    if url:
        profile = user.get_profile()
        avatar = urlopen(url).read()
        fout = open(filepath, "wb") #filepath is where to save the image
        fout.write(avatar)
        fout.close()
        profile.photo = url_to_image # depends on where you saved it
        profile.save()