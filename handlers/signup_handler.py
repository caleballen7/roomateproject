
import jinja_env
import logging
import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb

class NewUser(ndb.Model):
    clenliness = ndb.StringProperty()
    weekwake = ndb.StringProperty()
    weekndwake = ndb.StringProperty()



class SignUpHandler(webapp2.RequestHandler):
    def get(self):
        newuser = NewUser.query().fetch()

        new_user = ""
        for user in newuser:
            new_user += "<p>" + "You are " + str(user.clenliness) + " clean. You wake up around " + str(user.weekwake) + " during the week, and " + str(user.weekndwake) + " on the weekends. Here are people that you would be good roommates with!"



        template = jinja_env.env.get_template('templates/signup.html')

        user_params = {
            "html_info": new_user,
            }
        self.response.out.write(template.render(user_params))
        #connecting the response from multiple choice with a value
    def post(self):
        r_clean = self.request.get("form_clean")
        r_week = self.request.get("form_week")
        r_weeknd = self.request.get("form_weeknd")

        new_user = NewUser(clenliness = r_clean, weekwake = r_week, weekndwake = r_weeknd)
        new_user.put()
        self.redirect("/find")
        






        