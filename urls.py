from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^tourney/', include('naughty_nice.foo.urls')),
    (r'^tourney/?$', 'naughty_nice.views.index'),
    (r'^tourney/example.html$', 'naughty_nice.views.example'),

    (r'^tourney/static/css/(?P<theme>[^/]+)/images/(?P<filename>[^.]+).png$', 'naughty_nice.views.jquery_ui_images'),
    (r'^tourney/static/css/(?P<filename>.+)$', 'naughty_nice.views.css'),
    (r'^tourney/static/js/(?P<filename>.+)$', 'naughty_nice.views.js'),
    (r'^tourney/static/img/(?P<filename>[^.]+)\.gif$', 'naughty_nice.views.gif'),
    (r'^tourney/static/img/(?P<filename>[^.]+)\.png$', 'naughty_nice.views.png'),
    (r'^tourney/static/img/(?P<filename>[^.]+)\.(?P<extension>jpe?g)$', 'naughty_nice.views.jpeg'),

    (r'^tourney/', include('naughty_nice.tourney.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
