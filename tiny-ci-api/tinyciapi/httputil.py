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

class Response(object):
    def __init__(self, status, headers, body):
        self.status = status
        self.raw_headers = headers
        self.body = body
        self.headers = dict(headers)


class Request(object):
    def __init__(self, method, url):
        self._method = method
        self._url = url
        self._headers = {
            'User-Agent': 'tiny-ci'
        }
        self._payload = None

    def execute(self, expects = [200]):
        self._headers['User-Agent'] = self._headers.get('User-Agent', 'tiny-ci')
        parsed = urlparse(self._url)
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
            conn.request(self._method, uri, self._payload, self._headers)
            resp = conn.getresponse()
            body = resp.read()
            if resp.status not in expects:
                raise Error('Status: %d %s %sri' % (resp.status, resp.reason, body))
            return Response(resp.status, resp.getheaders(), body)
        finally:
            close(conn)


def __main():
    req = Request('GET', 'https://api.github.com/meta')
    resp = req.execute()
    print resp.status
    print resp.raw_headers
    print resp.headers['content-type']
    print resp.body
    #obj = req('GET', 'https://api.github.com/meta')
    #print obj

if __name__ == '__main__':
    __main()
