from django.views.generic import ListView

from monews.feeds.models import FeedItem


class Home(ListView):
    template_name = 'base/home.html'
    context_object_name = 'feed_items'

    def get_queryset(self):
        return FeedItem.objects.order_by('-published')
