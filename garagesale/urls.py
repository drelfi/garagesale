from django.conf.urls.defaults import patterns, url, include

from garagesale import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^p/(?P<cpartner>\w+)/$', views.index, name='partner-index'),
    url(r'^(?P<item_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<item_id>\d+)/contact/$', views.contact, name='contact'),

    url(r'^admin/', include(admin.site.urls)),
)
