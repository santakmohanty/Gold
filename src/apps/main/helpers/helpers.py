import os
import re
from datetime import datetime, time
from io import StringIO
from html.parser import HTMLParser

from django.template.defaultfilters import slugify

from project.settings import BASE_DIR


class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = StringIO()

    def handle_data(self, d):
        self.text.write(d)

    def get_data(self):
        return self.text.getvalue()

    def error(self, message):
        pass


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def clean_folder_path(path):
    path = path + '/' if not path.endswith('/') else path
    path = path + '/' if not path.startswith('/') else path
    return str(path)


def save_file(file, location):
    location = clean_folder_path(location)
    if not os.path.isdir(BASE_DIR + location):
        os.makedirs(BASE_DIR + location)

    file_name = file
    file_name, extension = os.path.splitext(str(file_name))
    extension = str(extension).strip('.')
    file_name = str(file_name)
    file_name = slugify(file_name)
    file_name = file_name.lower() + '-' + str(datetime.now().timestamp()).replace('.', '')

    with open(BASE_DIR + location  + file_name + '.' + extension, 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)
        f.close()

    return location + file_name + '.' + extension, file_name + '.' + extension


class InputValidation:
    STRING = r'^[a-zA-Z]+$'
    STRING_SPACE = r'^[a-zA-Z\s]+$'
    STRING_UPPERCASE = r'^[A-Z]+$'
    STRING_UPPERCASE_SPACE = r'^[A-Z\s]+$'
    STRING_LOWERCASE_SPACE = r'^[a-z\s]+$'
    NUMERIC = r'^[0-9]+$'
    ALPHA_NUMERIC = r'^[A-Za-z0-9]+$'
    ALPHA_NUMERIC_SPACE = r'^[A-Za-z0-9\s]+$'
    MOBILE_NUMBER = r'^[0-9]{10}+$'

    @classmethod
    def is_valid(cls, string, validation_type):
        return re.match(validation_type, string)


class QueueStatus:
    NEW = 10
    RUNNING = 20
    COMPLETE = 30
    ERROR = 40

    @classmethod
    def status_message(cls, status):
        if status == cls.NEW:
            return 'Queue Registered'
        elif status == cls.RUNNING:
            return 'Queue Running'
        elif status == cls.COMPLETE:
            return 'Queue Complete'
        elif status == cls.ERROR:
            return 'Queue Failed'
        else:
            return ''
