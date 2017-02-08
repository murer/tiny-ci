import httplib
import urllib
import urlparse
from jsonutil import JSON

class Error(Exception):
    """Exceptions"""

def close(obj):
    try:
        obj.close()
    except:
        """ Done """

class Response(object):
    def __init__(self, status, headers, body):
        self.status = status
        self.raw_headers = headers
        self.body = body
        self.headers = dict(headers)

    def body_json(self):
        return JSON.parse(self.body) if self.body else None

    def body_form_array(self):
        return urlparse.parse_qs(self.body)

    def body_form(self):
        return dict(urlparse.parse_qsl(self.body))

class Request(object):
    def __init__(self, method, url):
        self._method = method
        self._url = url
        self.headers = {
            'User-Agent': 'tiny-ci'
        }
        self._payload = None

    def send_form(self, payload):
        self.headers['Content-Type'] = self.headers.get('Content-Type', 'application/x-www-form-urlencoded')
        self._payload = urllib.urlencode(payload or {})
        return self

    def execute(self, expects = [200]):
        self.headers['User-Agent'] = self.headers.get('User-Agent', 'tiny-ci')
        parsed = urlparse.urlparse(self._url)
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
            conn.request(self._method, uri, self._payload, self.headers)
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
    print resp
    print dir(resp)
    print resp.status
    print resp.raw_headers
    print resp.headers['content-type']
    print resp.body_json()

if __name__ == '__main__':
    __main()
