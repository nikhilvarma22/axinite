#python imports
import os
import uuid
import datetime
import json
import urllib2 
from urllib2 import urlopen
from datetime import timedelta

#django imports
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import load_backend, login, logout
from django.conf import settings

#social auth
from social_auth.backends.facebook import FacebookBackend
from social_auth.backends.twitter import TwitterBackend


#axinite imports
from axinite.axusers.forms.login_form import LoginForm
from axinite.axusers.models import UserProfile
from axinite.axprofile.models import UserFriends
from axinite.settings import PROJECT_PATH
#------------------------------------------------------------------------------
def registration_confirmation(request):
    try:
        email = request.GET.get('email')
    except:
        email = ''
    return render_to_response('axusers/registration_confirmation.html',
                              {'email' : email})

#------------------------------------------------------------------------------
def registration_failure(request):
    return render_to_response('axusers/registration_failure.html')
#------------------------------------------------------------------------------
def verification_error(request):
    try:
        reason = request.GET.get('reason')
    except:
        reason = 'Invalid Key'
    return render_to_response('axusers/verification_error.html',
                              {'reason' : reason})
#------------------------------------------------------------------------------
def verify_registration(request):
    verified = False
    reason = 'Invalid Key'
    try:
        key = request.GET.get('key')
        username = request.GET.get('username')
        user = User.objects.get(username=username)
        user_key = user.profile.key
        key_validity = int(user.profile.key_expires.strftime('%s'))
        now = int(datetime.datetime.now().strftime('%s'))
        if not user.profile.key == key:
            verified = False
            reason = 'Unknown Key'
        if not key_validity > now:
            user.profile.delete()
            user.delete()
            verified = False
            reason = 'Key Expired'
        verified = True
    except Exception as e:
        print e.__str__()
        verified = False
    if not verified:
        return HttpResponseRedirect('/verification_error?reason=%s' % reason)
    else:
        user.is_locked = False
        user.save()
        user.profile.key = uuid.uuid4().__str__()
        user.profile.save()
        login_user(request, user)
        user.save()
        return HttpResponseRedirect('/axprofile')
#------------------------------------------------------------------------------
def login_user(request, user):
    """
    Log in a user without requiring credentials (using ``login`` from
    ``django.contrib.auth``, first finding a matching backend).

    """
    from django.contrib.auth import load_backend, login
    if not hasattr(user, 'backend'):
        for backend in settings.AUTHENTICATION_BACKENDS:
            if user == load_backend(backend).get_user(user.pk):
                user.backend = backend
                break
    if hasattr(user, 'backend'):
        return login(request, user)
#------------------------------------------------------------------------------    
def register_user(data):
    """
    This method is used to register a new user and create a user profile.
    """
    new_user = User.objects.create_user(data['username'], data['confirm_email'], 
                                        data['confirm_password'])
    new_user.first_name = data['first_name']
    new_user.last_name = data['last_name']
    new_user.email = data['email']
    new_user.is_locked = True
    new_user.save()
    profile = new_user.profile
    key = uuid.uuid4().__str__()
    profile.key = key
    profile.save()
    if new_user and profile:
        return new_user
    else:
        return False
#-------------------------------------------------------------------------------
def axlogin(request):
    login_form = LoginForm()
    return render_to_response('axusers/axlogin.html',
                              {'login_form' : login_form})

#-------------------------------------------------------------------------------
def axlogout(request):
    logout(request)
    return HttpResponseRedirect('/')
#-------------------------------------------------------------------------------
def login_error(request):
    return HttpResponseRedirect('axusers/login_error.html')
#-------------------------------------------------------------------------------
def get_user_avatar(backend, details, response, social_user, uid, user, *args, 
                    **kwargs):
    
    url = None
    if backend.__class__ == FacebookBackend:
        url = "http://graph.facebook.com/%s/picture?type=large" % response['id']
    elif backend.__class__ == TwitterBackend:
        url = response.get('profile_image_url', '').replace('_normal', '')
    if url:
        try:
            profile = UserProfile.objects.get(user=user.id)
        except:
            profile = None
        if not profile:
            profile = UserProfile(user=user)
        avatar = urlopen(url).read()
        filename = ('/media/profiles/profile%s.jpg' % (str(user.id)))
        filepath = PROJECT_PATH + filename
        with open(filepath, "wb") as avatar_file:
            avatar_file.write(avatar) 
        profile.profile_photo = filename 
        profile.save()
#-------------------------------------------------------------------------------
def get_user_friends(backend, details, response, social_user, uid, user, *args, 
                    **kwargs):
    url = None
    if backend.__class__ == FacebookBackend:
        friends_url = 'https://graph.facebook.com/%s/friends?access_token=%s' % \
        (response['id'], response['access_token'])
    elif backend.__class__ == TwitterBackend:
        pass
 
    if friends_url:
        try:
            UserFriends.objects.filter(id=id).delete()
        except:
            pass
        import sys, traceback
        try:
            friends = json.loads(urlopen(friends_url).read())
        except Exception as e:
            
            print "Exception in user code:"
            print '-'*60
            traceback.print_exc(file=sys.stdout)
            print '-'*60
            friends = None
        
        if friends:
            if friends['data']:
                friends = friends['data']
                try:
                    UserFriends.objects.filter(user=user).delete()
                except:
                    pass
                for friend in friends:
                    new_friend = UserFriends(user=user, 
                                             friend_name=friend['name'],
                                             friend_id=friend['id'],
                                             social_site=\
                                             backend.__class__.__name__)
                    new_friend.save()
                
    return False
#-------------------------------------------------------------------------------
            
            
        
        
        

