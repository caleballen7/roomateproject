from google.appengine.ext import ndb

class UserModel(ndb.Model):
    clenliness = ndb.StringProperty()
    weekwake = ndb.StringProperty()
    weekndwake = ndb.StringProperty()
    user_email = ndb.StringProperty()
    user_bio = ndb.StringProperty()
    form_first = ndb.StringProperty()
    form_last = ndb.StringProperty()
    dorm = ndb.StringProperty()
    gradyear = ndb.StringProperty()
    age = ndb.StringProperty()
    



