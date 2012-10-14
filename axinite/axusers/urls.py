from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    "axinite.axusers.views",
    
    (r'^axlogin/', 'axlogin'),
    (r'^verification_error/', 'verification_error'),
    (r'^verify_registration/', 'verify_registration'),
    (r'^registration_failure/', 'registration_failure'),
    url(r'^logout/', 'axlogout',name="logout"),
    url(r'^registration_confirmation/', 'registration_confirmation',name="registration_confirmation"),
    url(r'^registration/$', 'complete_registration',name="complete_registration"),
)