from google.appengine.ext import ndb

class Secret(ndb.Model):
    secret = ndb.StringProperty()
