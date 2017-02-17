from django.utils.cache import patch_vary_headers


class DoNotTrackMiddleware(object):

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
