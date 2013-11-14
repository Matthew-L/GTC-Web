from django.conf.urls import patterns, include, url
from pythonbackend.views import calculate, results
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^calculate/$', calculate),
    url(r'^results/$', results),

    # url(r'^$', 'mangoDjango.views.home', name='home'),
    # url(r'^mangoDjango/', include('mangoDjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # user accounts
    (r'^$', 'mangoDjango.views.login'),
    (r'^accounts/login/$', 'mangoDjango.views.login'),
    (r'^accounts/auth/$', 'mangoDjango.views.auth_view'),
    (r'^accounts/logout/$', 'mangoDjango.views.logout'),
    (r'^accounts/loggedin/$', 'mangoDjango.views.loggedin'),
    (r'^accounts/invalid/$', 'mangoDjango.views.invalid_login'),
    (r'^accounts/register/$', 'mangoDjango.views.register_user'),
    (r'^accounts/register_success/$', 'mangoDjango.views.register_success'),
)