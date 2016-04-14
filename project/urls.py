from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

import main.urls

urlpatterns = patterns('',
                     url(r'^', include('main.urls'))
                       )

urlpatterns += []

urlpatterns += patterns('', (r'^media\/(?P<path>.*)$',
                             'django.views.static.serve',
                             {'document_root': settings.STATIC_ROOT}),
                        )

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
