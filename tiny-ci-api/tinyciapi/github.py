import webutil
import logging as LOG

class WebhookHandler(webutil.RequestHandler):
    def post(self):
        LOG.info('querystring: %s' % (self.request.query_string))
        LOG.info('headers: %s' % (self.request.headers))
        LOG.info('content: %s' % (self.request.body))
        LOG.info('POST: %s' % (self.request.POST))
        LOG.info('GET: %s' % (self.request.GET))
        self.send_json("OK")
