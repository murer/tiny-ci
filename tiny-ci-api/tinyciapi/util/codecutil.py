import base64

def b64enc(data):
    return base64.b64encode(data)

def b64dec(data):
    return base64.b64decode(data)

def ub64enc(data):
    return base64.urlsafe_b64encode(data).rstrip('=')

def ub64dec(data):
    if isinstance(data, unicode):
        data = data.encode('utf-8', 'strict')
    r = len(data) % 4
    if r:
        r = 4 - r
        data += ('=' * r)
    return base64.urlsafe_b64decode(data)

def enc(data):
    return ub64enc(data)

def dec(data):
    return ub64dec(data)
