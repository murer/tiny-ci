import webapp2
import webutil
import github

class PingHandler(webutil.RequestHandler):
    def get(self):
        self.send_json("OK")

app = webapp2.WSGIApplication([
    ('/api/ping', PingHandler),
    ('/api/github/webhook', github.WebhookHandler)
])