from django.conf.urls import patterns, url

from monews.feeds import views


urlpatterns = patterns('',
    url(r'^/feeds/(?P<id>\d+)/$', views.FeedDetailView.as_view(), name='feeds.feed'),
    url(r'^/feeds/(?P<id>\d+)/items/$', views.FeedItemListView.as_view(), name='feeds.feed_items'),
)
