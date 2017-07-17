
import jinja_env
import logging
import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb
from models import newuser




class SignUpHandler(webapp2.RequestHandler):
    def get(self):

        template = jinja_env.env.get_template('templates/signup.html')

        self.response.out.write(template.render())

        #connecting the response from multiple choice with a value
    def post(self):
        r_clean = self.request.get("form_clean")
        r_week = self.request.get("form_week")
        r_weeknd = self.request.get("form_weeknd")
        r_email = self.request.get("form_email")

        new_user = newuser.UserModel(clenliness = r_clean, weekwake = r_week, weekndwake = r_weeknd)
        new_user.put()
        self.redirect("/find")








        