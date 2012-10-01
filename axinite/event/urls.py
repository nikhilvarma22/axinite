from django.conf.urls.defaults import *


urlpatterns = patterns(
    "axinite.event.views",
    
    (r'^createevent/$', 'eventcreation'),
)