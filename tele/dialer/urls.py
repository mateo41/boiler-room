from django.conf.urls import patterns, url

from dialer import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^call/$', views.call, name='call'),
    url(r'^incoming/$', views.incoming, name='incoming')
)
