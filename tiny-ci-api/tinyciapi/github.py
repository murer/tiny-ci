import webutil
import logging as LOG
from jsonutil import JSON
from google.appengine.api import taskqueue

# https://api.github.com/meta

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
