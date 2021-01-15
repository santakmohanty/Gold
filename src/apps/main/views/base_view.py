import logging
import sys
import traceback

from django.shortcuts import render
from django.views import View
from hashids import Hashids

from gold.settings import HASHIDS_SALT


def is_super_admin(func):
    # DECORATOR
    def wrapper(base_view_object, request, *args, **kwargs):
        if 'is_super_admin' in request.session:
            return func(base_view_object, request)
        else:
            return render(request, 'layouts/404.html', {})

    return wrapper


class BaseView(View):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    hashid = Hashids(salt=HASHIDS_SALT, min_length=7)

    # scheduler = Scheduler(connection = Redis())
    # queue = Queue(connection = Redis())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # def dispatch(self, request: HttpRequest, *args, **kwargs):
    #     uri = escape_uri_path(request.path)
    #     segments = uri.lstrip('/').rstrip('/').split('/')
    #     segment_count = len(segments)
    #     handler = None
    #     if segments[0] == 'app':
    #         if segment_count == 3:
    #             handler = getattr(self, segments[2], None)
    #             if handler is None:
    #                 handler = getattr(self, 'index', None)
    #         elif segment_count >= 4:
    #             handler = getattr(self, segments[3], None)
    #     else:
    #         if segments[segment_count - 1] == '':
    #             handler = getattr(self, 'index', None)
    #         else:
    #             handler = getattr(self, segments[segment_count - 1], None)
    #     if handler is not None:
    #         try:
    #             return handler(request)
    #         except Exception as e:
    #             raise e
    #     else:
    #         raise Http404()

    @classmethod
    def log_stack_trace(cls, error):
        trace = traceback.extract_tb(sys.exc_info()[2])
        # Add the event to the log
        output = "Error in the server: %s.\n" % (error)
        output += "\tTraceback is:\n"
        for (file, linenumber, affected, line) in trace:
            output += "\t> Error at function %s\n" % (affected)
            output += "\t  At: %s:%s\n" % (file, linenumber)
            output += "\t  Source: %s\n" % (line)
        output += "\t> Exception: %s\n" % (error)
        cls.logger.info('Exception Stack Trace')
        cls.logger.error(output)
        cls.logger.info('=========END=========')
