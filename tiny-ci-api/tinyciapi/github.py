import webutil

class WebhookHandler(webutil.RequestHandler):
    def get(self):
        self.send_json("OK")
