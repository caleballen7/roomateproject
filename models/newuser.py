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
    friends = ndb.StringProperty()
    noiselevel = ndb.StringProperty()
    bed = ndb.StringProperty()
    God = ndb.StringProperty()
    hotorcold = ndb.StringProperty()
    study = ndb.StringProperty()
    sex = ndb.StringProperty()
    sports=ndb.StringProperty()
    reading=ndb.StringProperty()
    game=ndb.StringProperty()
    netflix=ndb.StringProperty()
    tech=ndb.StringProperty()
    




