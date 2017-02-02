import webapp2
import webutil

class PingService(webutil.RequestHandler):
    def get(self):
        self.send_json("OK")

app = webapp2.WSGIApplication([
    ('/s/ping', PingService)
])
