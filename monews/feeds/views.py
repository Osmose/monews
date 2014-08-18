from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from monews.feeds.models import Feed


class FeedDetailView(DetailView):
    model = Feed
    template_name = 'feeds/feed.html'
    context_object_name = 'feed'


class FeedItemListView(ListView):
    template_name = 'feeds/feed_items.html'
    context_object_name = 'feed_items'

    def get_queryset(self):
        self.feed = get_object_or_404(Feed, id=self.kwargs['feed_id'])
        return self.feed.feeditem_set.order_by('-published')

    def get_context_data(self, **kwargs):
        ctx = super(FeedItemListView, self).get_context_data(**kwargs)
        ctx['feed'] = self.feed
        return ctx
