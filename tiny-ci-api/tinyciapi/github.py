import webutil
import webapp2
import logging as LOG
from jsonutil import JSON
from google.appengine.api import taskqueue

# https://api.github.com/meta

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
        self.send_json(code)

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
