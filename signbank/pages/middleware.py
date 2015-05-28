from views import page
from django.http import Http404
from django.conf import settings
from signbank.log import debug


class PageFallbackMiddleware(object):

    def process_response(self, request, response):
        if response.status_code != 404:
            # No need to check for a flatpage for non-404 responses.
            return response
        try:
            return page(request, request.path_info)
        # Return the original response if any errors happened. Because this
        # is a middleware, we can't assume the errors will be caught elsewhere.
        except Http404:
            return response
        except:
            if settings.DEBUG:
                raise
            return response
