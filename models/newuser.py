from google.appengine.ext import ndb

class UserModel(ndb.Model):
    clenliness = ndb.StringProperty()
    weekwake = ndb.StringProperty()
    weekndwake = ndb.StringProperty()
    user_email = ndb.StringProperty()


