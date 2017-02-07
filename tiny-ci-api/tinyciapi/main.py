import webapp2
import webutil
import githubhandler
import googlehandler

class PingHandler(webutil.RequestHandler):
    def get(self):
        self.send_json("OK")

app = webapp2.WSGIApplication([
    ('/api/ping', PingHandler),

    ('/api/github/oauthlogin', github.OAuthLoginHandler),
    ('/api/github/oauthcallback', github.OAuthCallbackHandler),
    ('/api/github/webhook', githubhandler.WebhookHandler),
    ('/api/github/consume', githubhandler.ConsumeHandler),

    ('/api/google/oauthlogin', googlehandler.OAuthLoginHandler),
    ('/api/google/oauthcallback', googlehandler.OAuthCallbackHandler)

])
