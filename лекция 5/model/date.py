import datetime

def cur():
    d = datetime.datetime.utcnow()
    return f"{d.year}-{d.month}-{d.day}"