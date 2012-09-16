# Create your views here.
from axinite.usermanagement.forms import SignUpForm
from django.shortcuts import render_to_response
from django.template import RequestContext


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