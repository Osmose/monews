from django.contrib.staticfiles.storage import staticfiles_storage

from jingo import register


@register.function
def static(path):
    """Return the URL for a staticfiles resource."""
    return staticfiles_storage.url(path)
