from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    url(r'^(?P<task_id>\d+)/$', detail),
)