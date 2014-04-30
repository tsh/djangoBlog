from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import Blog.views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'tag/(?P<tag>\w+)/', Blog.views.postByTag, name='postByTag'),
    url(r'^$', Blog.views.index, name='index'),
)
