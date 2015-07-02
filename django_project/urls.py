from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    url(r'^p/(?P<name>\w*)', 'home.views.index'),
    url(r'^$', 'home.views.index'),
    url(r'^create', 'home.views.create'),
    url(r'^admin/', include(admin.site.urls)),
)
