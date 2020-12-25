from django.contrib import messages
from django.http import HttpResponseRedirect, HttpRequest
from django.utils.encoding import escape_uri_path


def get_segments_from_uri(request):
    uri = escape_uri_path(request.path)
    segment_uri = uri.lstrip('/').rstrip('/')
    segments = [] if segment_uri == '' else segment_uri.split('/')
    segment_count = len(segments)

    return segments, segment_count


class AdminAuthMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.process_request(request)
        if response is None:
            # If process_request returned None, we must call the next middleware or
            # the view. Note that here, we are sure that self.get_response is not
            # None because this method is executed only in new-style middleware.
            response = self.get_response(request)

        response = self.process_response(request, response)
        return response

    @staticmethod
    def process_response(request, response):
        """Let's handle old-style response processing here, as usual."""
        # Do something with response, possibly using request.
        return response

    @staticmethod
    def process_request(request: HttpRequest):
        pass
