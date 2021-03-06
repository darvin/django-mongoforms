# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

entry_pattern = patterns('apps.blog.views',
    (r'^$', 'show'),
    (r'^edit/$', 'edit'),
    (r'^delete/$', 'delete'),
)

urlpatterns = patterns('apps.blog.views',
    (r'^$', 'index'),
    (r'^new/$', 'new'),
    (r'^(?P<slug>[\w\-]+)/', include(entry_pattern)),
    (r'^new_tag/(?P<tag_name>[\w\-]+)/$', 'new_tag'),

)