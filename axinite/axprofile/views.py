#django imports
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

#axinite imports
from axinite.axusers.models import *

@login_required()
def axprofile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user.id)
    hometown = profile.hometown
    education_history = UserEducation.objects.filter(user=user).order_by('year')
    list_education = []
    for education in education_history:
        list_education.append({
                              'school' : education.school,
                              'type' : education.type,
                              'degree' : education.degree,
                              'year' : education.year,
                              })
    
    work_history = UserWorkHistory.objects.filter(user=user)
    
    list_work = []
    for work in work_history:
        list_work.append({
                          'position' : work.position,
                          'employer' : work.employer,
                          'start_date' : work.start_date,
                          'location' : work.location,
                          })
    
    friends = UserFriends.objects.filter(user=user).order_by('friend_name')
    list_friends = []
    for friend in friends:
        list_friends.append(friend.friend_name)
    
    languages = UserLanguages.objects.filter(user=user).order_by('language')
    list_languages = []
    for language in languages:
        list_languages.append(language.language)
        
    list_religion = UserReligiousViews.objects.filter(user=user)
    religion = None
    for religion in list_religion:
        religion = religion.name

    list_political = UserPoliticalViews.objects.filter(user=user)
    political = None
    for political in list_political:
        political = political.description
    
    return render_to_response('axprofile/profile.html',
                              {'first_name' : user.first_name,
                               'last_name' : user.last_name,
                               'profile_photo' : profile.profile_photo,
                               'friends' : list_friends,
                               'list_education' : list_education,
                               'list_work' : list_work,
                               'list_languages' : list_languages,
                               'hometown' : hometown,
                               'religion' : religion,
                               'political' : political
                               })
    