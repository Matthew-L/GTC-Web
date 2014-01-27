from django.conf.urls import patterns, include, url
from pythonbackend.views import calculate
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    #url(r'^results/$', results),

    # url(r'^$', 'mangoDjango.views.home', name='home'),
    # url(r'^mangoDjango/', include('mangoDjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #url(r'^', include('favicon.urls')),

    # functionality
    (r'^calculate/$', calculate),
    (r'^delete-set/$', 'pythonbackend.views.deleteSet'),
    (r'^download-set', 'mangoDjango.views.downloadStringSet'),
    (r'^search/$', 'mangoDjango.views.search'),
    (r'^ajax/$', 'pythonbackend.views.ajax_calculate'),
    (r'^ajax-delete/$', 'pythonbackend.views.ajaxDeleteSet'),
    (r'^save-set/$', 'pythonbackend.views.save_set'),
    #(r'^is-valid-scale-length/$', 'pythonbackend.views.isValidScaleLength'),
    #(r'^is-valid-gauge/$', 'pythonbackend.views.isValidGauge'),
    #(r'^is-valid-string-number/$', 'pythonbackend.views.isValidStringNumber'),
    #(r'^is-valid-number-of-strings/$', 'pythonbackend.views.isValidNumberOfStrings'),
    (r'^info/$','mangoDjango.views.info'),

    # user accounts
    (r'^$', 'mangoDjango.views.login'),
    (r'^accounts/login/$', 'mangoDjango.views.login'),
    (r'^accounts/auth/$', 'mangoDjango.views.auth_view'),
    (r'^accounts/logout/$', 'mangoDjango.views.logout'),
    (r'^accounts/invalid/$', 'mangoDjango.views.invalid_login'),
    (r'^accounts/register/$', 'mangoDjango.views.register_user'),
    (r'^accounts/register_success/$', 'mangoDjango.views.register_success'),
    (r'^profile/$', 'mangoDjango.views.profile'),


    # ios user accounts
    (r'^ios/login/$', 'mangoDjango.views.iosLogin'),

    #(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/favicon.ico'}),

)
