from django.conf.urls import patterns, url

import main.views

urlpatterns = patterns('',
                       url(r'^$', main.views.index),
                       url(r'^contact/', main.views.contact, name="contact"),
                       url(r'^projects/', main.views.projects, name="projects"),
                       url(r'^project/(?P<project_name>.+?)/$', main.views.project, name="project"),
                       )