from django.conf.urls import patterns, url

from accounts import views

urlpatterns = patterns('', 
    url(r'^login/$', views.handle_login, name='login'), 
    url(r'^logout/$', views.handle_logout, name='logout') 
)
