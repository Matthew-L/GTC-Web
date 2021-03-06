from django.conf.urls import patterns, include, url
from django.contrib import admin
from calculator.views import SaveSet
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
                       # Admin
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),

                       # Calculate
                       (r'^calculate/$', 'calculator.views.load_calculate_page'),
                       (r'^calculate-tension/$', 'calculator.views.convert_input_to_tension'),
                       # (r'^save-set/$', 'calculator.views.asynchronous_save_set'),
                       (r'^save-set/', SaveSet.as_view()),

                       # Download
                       (r'^download-set', 'profile.views.downloadStringSet'),

                       # Search
                       (r'^search/$', 'search.views.search'),

                       # USERS

                       # Login
                       # (r'^accounts/login/$', 'users.views.login'),
                       # (r'^$', 'users.views.login'),
                       (r'^invalid-login/$', 'users.views.invalid_login'),
                       # Authorize user
                       # (r'^authorize-account/$', 'users.views.auth_view'),
                       (r'^login/$', 'users.views.login'),
                       # Logout
                       (r'^logout/$', 'users.views.logout'),
                       # Register
                       (r'^register/$', 'users.views.register_user'),

                       # Profile
                       (r'^profile/$', 'profile.views.profile'),
                       (r'^delete-set/$', 'profile.views.delete_set'),

                       # Contact
                       # (r'^contact/$', 'contact.views.load_contact_page'),

                       # Test
                       # (r'^test/$', 'contact.views.load_test_page'),
                       # (r'^base-bak/$', 'contact.views.load_base_bak_page'),
                       (r'^$', 'stringulator.views.load_homepage'),
)

