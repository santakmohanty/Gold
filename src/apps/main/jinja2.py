from datetime import datetime
import math
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

from project.settings import BASE_URL
from jinja2 import Environment

from apps.main.custom_jinja_filters import timestamp_to_date, length, string, hashid_encode,hashid_decode


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'base_url': BASE_URL,
        'QueueStatus': QueueStatus,
        'current_timestamp': math.ceil(datetime.now().timestamp())
    }, zip = zip)
    env.filters['timestamptodate'] = timestamp_to_date
    env.filters['length'] = length
    env.filters['string'] = string
    env.filters['hashid_encode'] = hashid_encode
    env.filters['hashid_decode'] = hashid_decode
    return env
