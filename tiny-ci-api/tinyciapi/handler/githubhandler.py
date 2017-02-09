import webapp2
import logging as LOG
from google.appengine.api import taskqueue
from tinyciapi.util import webutil
from tinyciapi.util.jsonutil import JSON
from tinyciapi.util.httputil import Request as HTTP
from tinyciapi.service.cryptservice import TokenMixin

# https://api.github.com/meta

class GithubToken(TokenMixin):
    def __init__(self):
        self.gh = None

class OAuthLoginHandler(webutil.RequestHandler):
    def get(self):
        self.send_redirect('https://github.com/login/oauth/authorize', {
            'client_id': 'ccfa4f997ce81263aa9b',
            'redirect_uri': 'https://tiny-ci.appspot.com/api/github/oauthcallback',
            'scope': 'repo'
        })

class OAuthCallbackHandler(webutil.RequestHandler):
    def get(self):
        code = self.request.GET['code']
        req = HTTP('POST', 'https://github.com/login/oauth/access_token')
        resp = req.send_form({
            'client_id': 'ccfa4f997ce81263aa9b',
            'client_secret': '5c7d21c0558bdb5b2b6c61a8d376a98c7a6ce792',
            'code': code,
            'redirect_uri': 'https://tiny-ci.appspot.com/api/github/oauthcallback'
        }).execute()
        ret = GithubToken()
        ret.gh = resp.body_form()['access_token']
        self.send_json(ret.enc())

class WebhookHandler(webutil.RequestHandler):
    def post(self):
        LOG.info('remove: %s' % (self.request.remote_addr))
        LOG.info('headers: %s' % (self.request.headers))
        body = self.read_json()
        LOG.info('content: %s' % (JSON.stringify(body, indent=True)))
        task = taskqueue.add(
            queue_name = 'pushs',
            method = 'POST',
            url = '/api/github/consume',
            headers = {
                'Content-Type': 'application/json; charset=UTF-8'
            },
            payload = JSON.stringify(body))
        LOG.info('Task created: %s, eta: %s' % (task.name, task.eta))
        self.send_json(task.name)

class ConsumeHandler(webutil.RequestHandler):
    def post(self):
        body = self.read_json()
        LOG.info('content: %s' % (JSON.stringify(body, indent=True)))
        self.send_json('OK')
