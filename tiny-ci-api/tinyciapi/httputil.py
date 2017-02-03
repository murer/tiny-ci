import httplib
import urllib
from jsonutil import JSON
from urlparse import urlparse

class Error(Exception):
	"""Exceptions"""

def close(obj):
	try:
		obj.close()
	except:
		""" Done """

def req(method, url, headers = {}, payload = '', expects = [200]):
    headers['User-Agent'] = headers.get('User-Agent', 'tiny-ci')
    parsed = urlparse(url)
    host = parsed.netloc
    uri = parsed.path
    if(parsed.query != ''):
        uri = uri + '?' + parsed.query
    conn = None
    if(parsed.scheme == 'https'):
        conn = httplib.HTTPSConnection(parsed.hostname, parsed.port or 443)
    else:
        conn = httplib.HTTPConnection(parsed.hostname, parsed.port or 80)
    try:
        if method == 'POST' or method == 'PUT':
            headers['Content-Type'] = headers.get('Content-Type', 'application/x-www-form-urlencoded;charset=UTF-8')
        if isinstance(payload, dict) and headers['Content-Type'] == 'application/x-www-form-urlencoded;charset=UTF-8':
            payload = urllib.urlencode(payload)
        if isinstance(payload, dict) and headers['Content-Type'] == 'application/json':
            payload = JSON.stringify(payload)
        conn.request(method, uri, payload, headers)
        response = conn.getresponse()
        body = response.read()
        if response.status not in expects:
            raise Error('Status: %d %s %sri' % (response.status, response.reason, body))
        return body
    finally:
        close(conn)


def __main():
    obj = req('GET', 'https://api.github.com/meta')
    print obj

if __name__ == '__main__':
    __main()
