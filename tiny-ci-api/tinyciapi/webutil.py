from jsonutil import JSON
import webapp2


class RequestHandler(webapp2.RequestHandler):

    def send(self, obj, contentType, charset = None):
        self.response.content_type = contentType
        self.response.charset = charset
        self.response.write(obj)

    def send_json(self, obj):
        obj = JSON.stringify(obj)
        self.send(obj, 'application/json', 'utf-8')
