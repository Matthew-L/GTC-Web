from django.conf.urls import patterns, include, url

# from calculator.views import calculate

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

    (r'^calculate/$', 'calculator.views.calculate'),
    (r'^download-set', 'users.views.downloadStringSet'),
    (r'^search/$', 'users.views.search'),
    (r'^ajax/$', 'calculator.views.ajax_calculate'),
    (r'^ajax-delete/$', 'calculator.views.ajax_delete_set'),
    (r'^save-set/$', 'calculator.views.save_set'),
    (r'^info/$', 'users.views.info'),

    # user accounts
    (r'^$', 'users.views.login'),
    (r'^accounts/login/$', 'users.views.login'),
    (r'^accounts/auth/$', 'users.views.auth_view'),
    (r'^accounts/logout/$', 'users.views.logout'),
    (r'^accounts/invalid/$', 'users.views.invalid_login'),
    (r'^accounts/register/$', 'users.views.register_user'),
    (r'^accounts/register_success/$', 'users.views.register_success'),
    (r'^profile/$', 'users.views.profile'),

    (r'^contact/$', 'users.views.contact'),
    # (r'^bootstrap/$', 'mangoDjango.views.bootstrap'),
    # ios user accounts
    # (r'^ios/login/$', 'mangoDjango.views.iosLogin'),
    # url(r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': '../stringulator/static'}),
    #(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/favicon.ico'}),

)
