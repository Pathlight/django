import datetime

from django.utils.timezone import utc


def utc_tzinfo_factory(offset):
    if isinstance(offset, datetime.timedelta):
        # Turn the timedelta object into the int django expects
        offset = offset.total_seconds() // (60*60)
    if offset != 0:
        raise AssertionError("database connection isn't set to UTC")
    return utc
