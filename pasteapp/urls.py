from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from paste.views import *

urlpatterns = patterns('',
    url('^paste/$', AddSnippetView.as_view()),
    url('^syntax/$', SyntaxView.as_view()),
    url('^(?P<slug>[\w\d]+)$', SnippetView.as_view()),
    url('^(?P<slug>[\w\d]+)/delete/$', DeleteSnippetView.as_view()),
    url('^(?P<a>[\w\d]+)...(?P<b>[\w\d]+)$', DiffView.as_view()),
    url('^$', IndexView.as_view()),
    url(r'^social/', include('socialregistration.urls',
        namespace = 'socialregistration')),
    # Examples:
    # url(r'^$', 'pasteapp.views.home', name='home'),
    # url(r'^pasteapp/', include('pasteapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls))
)

