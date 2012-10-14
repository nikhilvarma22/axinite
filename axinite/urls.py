#django imports
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

#apps imports
#from axinite.home.views import home
#from axinite.axusers.views import registration_confirmation
#from axinite.axusers.views import registration_failure
#from axinite.axusers.views import verify_registration
#from axinite.axusers.views import verification_error
#from axinite.axusers.views import axlogin
#from axinite.axusers.views import axlogout
#from axinite.axusers.views import login_error
#from axinite.axprofile.views import axprofile

#-------------------------------------------------------------------------------
urlpatterns = patterns('',
    url(r'^$', 'home.views.home', name='home'),
    url(r'^axprofile/', include('axprofile.urls')),
    #url(r'^logout/', axlogout),
    url(r'^axusers/', include('axusers.urls')),
    #url(r'^login_error/', login_error),
    url(r'', include('social_auth.urls')),
    url(r'^event/', include('event.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
)
