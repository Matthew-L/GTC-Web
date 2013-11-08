from django.conf.urls import patterns, include, url
from article.views import HelloTemplate
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^articles/', include('article.urls')),
    url(r'^hello/$', 'article.views.hello'),
    url(r'^hello-template/$', 'article.views.hello_template'),
    url(r'^hello-class/$', HelloTemplate.as_view()),
    url(r'^hello-simple/$', 'article.views.hello_template_simple'),
    # url(r'^$', 'mangoDjango.views.home', name='home'),
    # url(r'^mangoDjango/', include('mangoDjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
