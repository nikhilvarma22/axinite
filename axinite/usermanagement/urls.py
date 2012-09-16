from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    "axinite.usermanagement.views",
        
    (r'^signup/', 'accountcreation'),
    
)
