from django.conf.urls import patterns, url

from monews.base import views


urlpatterns = patterns('',
    url(r'^$', views.home, name='base.home'),
)
