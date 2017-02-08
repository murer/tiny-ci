from tinyciapi.util import webutil
from tinyciapi.util.httputil import Request as HTTP

class OAuthLoginHandler(webutil.RequestHandler):
    def get(self):
        self.send_redirect('https://accounts.google.com/o/oauth2/v2/auth', {
            'response_type': 'code',
            'scope': 'https://www.googleapis.com/auth/compute',
            'redirect_uri': '%s/api/google/oauthcallback' % (self.request.host_url),
            'client_id': '235531131885-ksue4g0hjtfobgh1khtq51q77coetehg.apps.googleusercontent.com',
            'access_type': 'offline',
            'prompt': 'consent'
        })

class OAuthCallbackHandler(webutil.RequestHandler):
    def get(self):
        code = self.request.GET['code']
        req = HTTP('POST', 'https://www.googleapis.com/oauth2/v4/token')
        resp = req.send_form({
            'client_id': '235531131885-ksue4g0hjtfobgh1khtq51q77coetehg.apps.googleusercontent.com',
            'client_secret': 'bGxvF2S9EO5gnkjyADrWr-DW',
            'code': code,
            'redirect_uri': '%s/api/google/oauthcallback' % (self.request.host_url),
            'grant_type': 'authorization_code'
        }).execute()
        self.send_json(resp.body_json())
