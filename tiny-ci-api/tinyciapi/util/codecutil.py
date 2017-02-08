import base64

def b64enc(data):
    return base64.urlsafe_b64encode(data).rstrip('=')

def b64dec(data):
    b = 4 - (len(data) % 4)
    if b < 4:
        data += (b * '=')
    return base64.b64decode(data)
