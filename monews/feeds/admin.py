from django.contrib import admin

from monews.feeds import models


class FeedModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'feed_url', 'title', 'link', 'published')
    readonly_fields = ('title', 'link', 'description', 'published')
    search_fields = ('title', 'name', 'description', 'link', 'url')


class FeedItemModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'feed', 'published', 'guid')
    readonly_fields = ('title', 'link', 'description', 'published', 'guid')
    search_fields = ('title', 'description', 'link', 'guid')


admin.site.register(models.Feed, FeedModelAdmin)
admin.site.register(models.FeedItem, FeedItemModelAdmin)
