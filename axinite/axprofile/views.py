#django imports
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import  RequestContext
from django.contrib.auth.models import User

#axinite imports
from axinite.axusers.models import UserProfile
from axinite.axprofile.models import UserFriends

@login_required()
def axprofile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    friends = UserFriends.objects.filter(user=user).order_by('friend_name')
    list_friends = []
    for friend in friends:
        list_friends.append(friend.friend_name)
    return render_to_response('axprofile/profile.html',
                              {'first_name' : user.first_name,
                               'last_name' : user.last_name,
                               'profile_photo' : profile.profile_photo,
                               'friends' : list_friends
                               },
                              context_instance = RequestContext(request)
                              )