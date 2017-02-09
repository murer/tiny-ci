import webapp2
from util import webutil
from handler import githubhandler
from handler import googlehandler

class PingHandler(webutil.RequestHandler):
    def get(self):
        self.send_json("OK")

app = webapp2.WSGIApplication([
    ('/api/ping', PingHandler),

    ('/api/github/oauthlogin', githubhandler.OAuthLoginHandler),
    ('/api/github/oauthcallback', githubhandler.OAuthCallbackHandler),
    ('/api/github/webhook', githubhandler.WebhookHandler),
    ('/api/github/consume', githubhandler.ConsumeHandler),
    ('/api/github/computeurl', githubhandler.ComputeURLHandler),

    ('/api/google/oauthlogin', googlehandler.OAuthLoginHandler),
    ('/api/google/oauthcallback', googlehandler.OAuthCallbackHandler)

])
