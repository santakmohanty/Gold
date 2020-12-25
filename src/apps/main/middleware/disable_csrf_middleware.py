import re


class DisableCSRFMiddleware(object):
    # EXEMPTED_PATHS_REGULAR_EXPRESSION = [r"\/api\/meta-data\/[a-zA-Z0-9]+\/"] Example
    EXEMPTED_PATHS_REGULAR_EXPRESSION = []

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'POST':
            for pattern in DisableCSRFMiddleware.EXEMPTED_PATHS_REGULAR_EXPRESSION:
                if re.match(pattern, request.path):
                    setattr(request, '_dont_enforce_csrf_checks', True)
        response = self.get_response(request)
        return response
