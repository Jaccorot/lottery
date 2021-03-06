from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'lottery.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^zhixuan/', 'lottery.apps.website.views.index', name='index'),
    url(r'^$', 'lottery.apps.website.views.index', name='index'),
    url(r'^spider(?P<year>\d+)/', 'lottery.apps.website.views.spider', name='spider'),
    url(r'^spider/', 'lottery.apps.website.views.spider', name='spider'),
)
