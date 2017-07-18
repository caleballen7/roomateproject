from google.appengine.ext import ndb

class UserModel(ndb.Model):
    clenliness = ndb.StringProperty()
    weekwake = ndb.StringProperty()
    weekndwake = ndb.StringProperty()
    user_email = ndb.StringProperty()
    form_bio = ndb.StringProperty()
    form_first = ndb.StringProperty()
    form_last = ndb.StringProperty()
    dorm = ndb.StringProperty()
    gradyear = ndb.StringProperty()
    age = ndb.StringProperty()
    insta = ndb.StringProperty()
    twitter = ndb.StringProperty()
    petpeeves = ndb.StringProperty()




