#django imports
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

@login_required()
def axprofile(request):
    user = request.user
    
    return render_to_response('axprofile/profile.html',
                              {'first_name' : user.first_name,
                               'last_name' : user.last_name})