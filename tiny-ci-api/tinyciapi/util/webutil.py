from jsonutil import JSON
import webapp2
import urllib

class RequestHandler(webapp2.RequestHandler):

    def send(self, obj, contentType, charset = None):
        self.response.content_type = contentType
        self.response.charset = charset
        self.response.write(obj)

    def send_json(self, obj):
        obj = JSON.stringify(obj)
        self.send(obj, 'application/json', 'utf-8')

    def read_json(self):
        return JSON.parse(self.request.body) if self.request.body else None

    def send_redirect(self, url, params = None):
        params = urllib.urlencode(params) if params else None
        if not params:
            return self.redirect(url)
        if params.find('?') >= 0:
            return self.redirect('%s&%s' % (url, params))
        return self.redirect('%s?%s' % (url, params))
