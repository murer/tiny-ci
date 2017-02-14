from google.appengine.ext import ndb

class User(ndb.Model):
    githubUser = ndb.StringProperty(indexed = False)
    githubToken = ndb.StringProperty(indexed = False)

class Secret(ndb.Model):
    secret = ndb.StringProperty(indexed = False)
