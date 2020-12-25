from datetime import datetime

from hashids import Hashids

from project.settings import HASHIDS_SALT


def timestamp_to_date(timestamp):
    date = datetime.fromtimestamp(int(timestamp))
    return date.strftime('%d, %b %Y %I:%M %p')


def length(ls):
    return len(ls)


def string(val):
    return str(val)


def hashid_encode(val):
    _hashid = Hashids(salt = HASHIDS_SALT, min_length = 7)
    return _hashid.encode(val)

def hashid_decode(val):
    _hashid = Hashids(salt = HASHIDS_SALT, min_length = 7)
    return _hashid.decode(val)[0]