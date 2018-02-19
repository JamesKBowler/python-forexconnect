from datetime import datetime, timedelta

def ole_zero():
    return datetime(1899,12,30)

def to_ole(pydate):
    if isinstance(pydate, datetime):
        delta = pydate - ole_zero()
        return float(delta.days) + (float(delta.seconds) / 86400)
    else:
        return pydate

def fm_ole(oletime):
    if isinstance(oletime, float):
        return ole_zero() + timedelta(days=float(oletime))
    else:
        return oletime
    
def fm_string(dt_string, millisecond=False):
    """
    Input a date string and returns a datetime object.
    """
    if millisecond:
        return datetime.strptime(
            dt_string, '%Y/%m/%d %H:%M:%S.%f')
    else:
        return datetime.strptime(
            dt_string, '%Y/%m/%d %H:%M:%S')
