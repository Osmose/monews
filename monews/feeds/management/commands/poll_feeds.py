import time
from datetime import datetime

from django.core.management.base import BaseCommand
from django.utils import timezone

import feedparser

from monews.feeds.models import Feed, FeedItem


def _localtime_to_datetime(localtime):
    utctime = time.gmtime(time.mktime(localtime))
    naive_datetime = datetime(*utctime[:6])
    return timezone.make_aware(naive_datetime, timezone.utc)


class Command(BaseCommand):
    help = 'Poll feeds for new items.'

    def handle(self, *args, **kwargs):
        for feed in Feed.objects.all():
            self.stdout.write('Polling feed `{0}`'.format(feed.name))
            d = feedparser.parse(feed.feed_url)

            # Update feed details.
            for field in ('title', 'link', 'description'):
                if field in d.feed:
                    setattr(feed, field, d.feed[field])

            if 'published_parsed' in d.feed:
                feed.published = _localtime_to_datetime(d.feed.published_parsed)

            # Create new entries.
            for entry in d.entries:
                if 'id' not in entry:
                    self.stdout.write('Ignoring feed entry: missing guid.')
                    continue

                feed_item, created = FeedItem.objects.get_or_create(feed=feed, guid=entry.id)
                for field in ('title', 'link', 'description'):
                    if field in entry:
                        setattr(feed_item, field, entry[field])

                if 'published_parsed' in entry:
                    feed_item.published = _localtime_to_datetime(entry.published_parsed)

                feed_item.save()

        self.stdout.write('Done!')
