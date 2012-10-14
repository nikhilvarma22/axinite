from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    "axinite.event.views",
    
    (r'^createevent/$', 'eventcreation'),
)