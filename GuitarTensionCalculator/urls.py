from django.conf.urls import patterns, include, url
from GTC.views import hello, current_datetime, index, calculate
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   url(r'^hello/$', hello),
   url(r'^time/$', current_datetime),
   url(r'^index/$', index),
   url(r'^calculate/$', calculate),


   # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
