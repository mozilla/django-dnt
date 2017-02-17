from django.utils.cache import patch_vary_headers

try:
    # Added in Django 1.10
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    _base_class = object  # pragma: no cover
else:
    _base_class = MiddlewareMixin  # pragma: no cover


class DoNotTrackMiddleware(_base_class):

    def process_request(self, request):
        """
        Sets flag request.DNT based on DNT HTTP header.
        """
        if 'HTTP_DNT' in request.META and request.META['HTTP_DNT'] == '1':
            request.DNT = True
        else:
            request.DNT = False

    def process_response(self, request, response):
        """
        Adds a "Vary" header for DNT, useful for caching.
        """
        patch_vary_headers(response, ['DNT'])

        return response
