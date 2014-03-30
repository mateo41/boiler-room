from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^dialer/', include('dialer.urls')),
    url(r'^dialer/accounts/', include('accounts.urls')),
    url(r'^dialer/admin/', include(admin.site.urls)),
)
