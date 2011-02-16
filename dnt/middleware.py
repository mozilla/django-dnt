class DoNotTrackMiddleware(object):
    """Sets request.dnt to True or False based on the presence of the
    DNT HTTP header."""
    def process_request(self, request):
        if 'HTTP_DNT' in request.META and request.META['HTTP_DNT'] == '1':
            request.DNT = True
        else:
            request.DNT = False
