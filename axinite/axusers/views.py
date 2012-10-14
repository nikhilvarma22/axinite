#python imports
import os
import uuid
import datetime
import json
import urllib2 
from urllib2 import urlopen
from datetime import timedelta
import sys, traceback

#django imports
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import load_backend, login, logout
from django.conf import settings
from django.template import RequestContext

#social auth
from social_auth.backends.facebook import FacebookBackend
from social_auth.backends.twitter import TwitterBackend


#axinite imports
from axinite.axusers.forms.login_form import LoginForm
from axinite.axusers.models import *
from axinite.settings import PROJECT_PATH
from axinite.axusers.forms.additionalsignup_form import AdditionalSignUpform
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
        key_validity = int(user.profile.key_expires.strftime('%f'))
        now = int(datetime.datetime.now().strftime('%f'))
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
        verified = False
    if not verified:
        return HttpResponseRedirect('/axusers/verification_error?reason=%s' % reason)
    else:
        user.is_locked = False
        user.save()
        user.profile.key = uuid.uuid4().__str__()
        user.profile.save()
        login_user(request, user)
        user.save()
        return HttpResponseRedirect('/axusers/registration/')
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
                              {'login_form' : login_form},
                              context_instance = RequestContext(request)
                              )

#-------------------------------------------------------------------------------
def axlogout(request):
    logout(request)
    return HttpResponseRedirect('/')
#-------------------------------------------------------------------------------
def login_error(request):
    return HttpResponseRedirect('axusers/login_error.html')
#-------------------------------------------------------------------------------
#USER DATA FROM SOCIAL SITES
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
        except Exception as e:
            profile = UserProfile(user=user)
            
        avatar = urlopen(url).read()
        filename = ('/media/profiles/profile%s.jpg' % (str(user.id)))
        filepath = PROJECT_PATH + filename
        with open(filepath, "wb") as avatar_file:
            avatar_file.write(avatar) 
        profile.profile_photo = filename 
        profile.save()
#-------------------------------------------------------------------------------        
def get_user_info(backend, details, response, social_user, uid, user, *args, 
                    **kwargs):
    url = None
    if backend.__class__ == FacebookBackend:
        userinfo_url = 'https://graph.facebook.com/%s?access_token=%s' % \
        (response['id'], response['access_token'])
    elif backend.__class__ == TwitterBackend:
        pass
 
    if userinfo_url:
        try:
            userinfo = json.loads(urlopen(userinfo_url).read())
        except Exception as e:
            userinfo = None
        print userinfo
        
        #-----------------------------------------------------------------------
        #personal info
        try:
            user.first_name = userinfo['first_name']
            user.first_name = userinfo['last_name']
            try:
                profile = UserProfile.objects.get(user=user.id)
            except:
                profile = UserProfile(user=user)

            try:
                profile.gender = userinfo['gender']
            except: 
                pass
                
            try:
                profile.hometown = userinfo['hometown']['name']
            except: 
                pass
                
            try:
                profile.aboutme = userinfo['bio']
                
            except: 
                pass
                
            try:
                profile.current_location = userinfo['location']['name']
                
            except: 
                pass
            
            try:
                profile.birthday = userinfo['birthday']
            except: 
                pass
            
            profile.save()
            user.save()
        except Exception as e:
            print "Exception in user code:"
            print '-'*60
            traceback.print_exc(file=sys.stdout)
            print '-'*60
        #-----------------------------------------------------------------------
        #education history
        try:
            try:
                UserEducation.objects.filter(user=user).delete()
            except:
                pass
            list_education = userinfo['education']
            if list_education:
                for education in list_education:
                    school = ""
                    try:
                        school = education['school']['name']
                    except: 
                        pass    
                    type = ""
                    
                    try:
                        type = education['type']
                    except: 
                        pass    

                    degree = ""
                    try:
                        degree = education['degree']['name']
                    except: 
                        pass    

                    year = "" 
                    try:
                        year = education['year']['name']
                    except: 
                        pass    
                        
                    education = UserEducation(user=user, school=school, 
                                              type=type, degree=degree, 
                                              year=year)
                    education.save()
        except Exception as e:
            print "Exception in user code:"
            print '-'*60
            traceback.print_exc(file=sys.stdout)
            print '-'*60
            pass
        
        #-----------------------------------------------------------------------
        #work history
        try:
            try:
                UserWorkHistory.objects.filter(user=user).delete()
            except:
                pass
            list_work = userinfo['work']
            if list_work:
                for work in list_work:
                    position = ""
                    try:
                        position = work['position']['name']
                    except:
                        pass
                    
                    employer = ""
                    try:
                        employer = work['employer']['name']
                    except:
                        pass

                    start_date = ""
                    try:
                        start_date = work['start_date']
                    except:
                        pass

                    location = "" 
                    try:
                        location = work['location']['name']
                    except:
                        pass

                    work = UserWorkHistory(user=user, position=position, 
                                           employer=employer,
                                           start_date=start_date, 
                                           location=location)
                    work.save()
        except Exception as e:
            print "Exception in user code:"
            print '-'*60
            traceback.print_exc(file=sys.stdout)
            print '-'*60
        #-----------------------------------------------------------------------
        #languages 
        try:
            try:
                UserLanguages.objects.filter(user=user).delete()
            except:
                pass
            try:
                list_languages = userinfo['languages']
                if list_languages:
                    for language in list_languages:
                        language = UserLanguages(user=user, 
                                                 language=language['name'])
                        language.save()
            except:
                pass

        except Exception as e:
            print "Exception in user code:"
            print '-'*60
            traceback.print_exc(file=sys.stdout)
            print '-'*60
        #-----------------------------------------------------------------------
        #political
        try:
            UserPoliticalViews.objects.filter(user=user).delete()
        except:
            pass
        
        try:
            political = userinfo['political']
            political = UserPoliticalViews(user=user,description=political)
            political.save()
        except:
            pass

        #-----------------------------------------------------------------------
        #religion
        try:
            UserReligiousViews.objects.filter(user=user).delete()
        except:
            pass
        try:
            religion = userinfo['religion']
            religion = UserReligiousViews(user=user,name=religion, description="")
            religion.save()
        except:
            pass
#-------------------------------------------------------------------------------
def get_user_friends(backend, details, response, social_user, uid, user, *args, 
                    **kwargs):
    friends_url = None
    if backend.__class__ == FacebookBackend:
        friends_url = 'https://graph.facebook.com/%s/friends?access_token=%s&fields=name,id,picture' % \
        (response['id'], response['access_token'])
    elif backend.__class__ == TwitterBackend:
        pass
 
    if friends_url:
        try:
            UserFriends.objects.filter(id=id).delete()
        except:
            pass
        try:
            friends = json.loads(urlopen(friends_url).read())
        except Exception as e:
            friends = None
        
        if friends:
            if friends['data']:
                friends = friends['data']
                try:
                    UserFriends.objects.filter(user=user).delete()
                except:
                    pass
                for friend in friends:
                    try:
                        pic = friend['picture']['data']['url']
                    except:
                        pic = ""
                    new_friend = UserFriends(user=user, 
                                             friend_name=friend['name'],
                                             friend_id=friend['id'],
                                             pic=pic,
                                             social_site=\
                                             backend.__class__.__name__)
                    new_friend.save()
                
    return False
#-------------------------------------------------------------------------------
def complete_registration(request):
    """
    this function takes the addional signup details from user
    and save into the database.
    """
    if request.method == "POST":
        form = AdditionalSignUpform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            nationality = cd['nationality']
            location = cd['location']
            
            company_name = cd['company_name']
            designation = cd['designation']
            date_of_joining = cd['date_of_joining']
            date_of_leaving = cd['date_of_leaving']
            # Education History
            degree = cd['qualification_level']
            school = cd['university']
            branch = cd['branch']
            year_of_passout = cd['year_of_passout']
            
            
            
            for interests in cd['interest']:
                userprofile_obj.interest.add(interests.id)
            return HttpResponseRedirect('axusers/axprofile')
                
        else:
            print "Form is invalid"
    else:
        form = AdditionalSignUpform()
    return render_to_response("axprofile/profile2.html",
                            {'form':form},
                            context_instance=RequestContext(request)
                            )
    
    
            
        
        
        

