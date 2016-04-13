from django.conf.urls import patterns, url

import main.views

urlpatterns = patterns('',
                       (r'^$', main.views.index)
                       )