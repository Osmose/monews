from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

import bleach
from readability import Document


class Feed(models.Model):
    name = models.CharField(max_length=255, blank=False)

    feed_url = models.URLField(blank=False)
    title = models.CharField(max_length=255, blank=True)
    link = models.URLField(blank=True)
    description = models.TextField(blank=True)
    published = models.DateTimeField(blank=True, null=True)

    readable_description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if self.description:
            document = Document(self.description)
            self.readable_description = document.summary(html_partial=True)

        return super(Feed, self).save(*args, **kwargs)

    @property
    def bleached_readable_description(self):
        return bleach.clean(self.readable_description, tags=settings.ALLOWED_TAGS, strip=True)

    def get_absolute_url(self):
        return reverse('feeds.feed', args=(self.id,))

    def __unicode__(self):
        return self.name


class FeedItem(models.Model):
    feed = models.ForeignKey(Feed)

    guid = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255, blank=True)
    link = models.URLField(blank=True)
    description = models.TextField(blank=True)
    published = models.DateTimeField(blank=True, null=True)

    readable_description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if self.description:
            document = Document(self.description)
            self.readable_description = document.summary(html_partial=True)

        return super(FeedItem, self).save(*args, **kwargs)

    @property
    def bleached_readable_description(self):
        return bleach.clean(self.readable_description, tags=settings.ALLOWED_TAGS, strip=True)

    def __unicode__(self):
        return self.title
