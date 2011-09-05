#!/usr/bin/env/python
"""
Convert an ISO-8601 date string to the miliseconds from the epoch 
integer required by the Extended JSON format used by MongoDB [1]

[1] http://www.mongodb.org/display/DOCS/Mongo+Extended+JSON

Usage::

    >>> datestr2milis('2008-04-01T03:28:50.625999')
    1207020530625
    >>> datestr2milis('1970-01-01T00:00:01.000')
    1000
    >>> datestr2milis('1970-01-01T00:00:12.345')
    12345
    >>> datestr2milis('1970-01-01T00:00:59.999')
    59999
    >>> datestr2milis('1970-01-01T00:01:00.000')
    60000
"""

import calendar
from datetime import datetime

# ISO-8601 format extended to include fractions of seconds
# used by OpenLibrary JSON dumps
ISO_8601 = '%Y-%m-%dT%H:%M:%S'
ISO_8601_EXTENDED = ISO_8601 + '.%f'

def datestr2milis(dt_str):
    # (1) parse extended date string to build a datetime instance
    dt_obj = datetime.strptime(dt_str, ISO_8601_EXTENDED)
    # (2) make an UTC time tuple, losing fractional part of seconds,
    # (3) then convert the time tuple to integer seconds from the epoch
    dt_secs = calendar.timegm(dt_obj.utctimetuple())
    # (4) divide microseconds by 1000 and add to miliseconds from the epoch
    return int(float(dt_obj.microsecond)/1000 + dt_secs * 1000)

if __name__=='__main__':
    import doctest
    doctest.testmod()
