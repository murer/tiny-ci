import webutil
import logging as LOG

class WebhookHandler(webutil.RequestHandler):
    def post(self):
        LOG.info('remove: %s' % (self.request.remote_addr))
        LOG.info('headers: %s' % (self.request.headers))
        body = self.read_json()
        LOG.info('content: %s' % (body))
        self.send_json("OK1")
