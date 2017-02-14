from google.appengine.ext import ndb

class User(ndb.Model):
    githubId = ndb.IntegerProperty(indexed = False)
    githubToken = ndb.StringProperty(indexed = False)

class Secret(ndb.Model):
    secret = ndb.StringProperty(indexed = False)
