from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    
    # url(r'^$', 'axinite.views.home', name='home'),
    (r'^$', 'axinite.usermanagement.views.registration'),
    (r'^verify/', 'axinite.usermanagement.views.verify_registration'),
    (r'^invalid_key/', 'axinite.usermanagement.views.invalid_key'),
    (r'^email_sent/', 'axinite.usermanagement.views.email_sent'),
    (r'^profile/', 'axinite.usermanagement.views.profile'),
    (r'^login/', 'axinite.usermanagement.views.login_user'),
    url(r'^axinite/', include('axinite.usermanagement.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
