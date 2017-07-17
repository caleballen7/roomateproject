
import jinja_env
import logging
import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb
from models import newuser




class SignUpHandler(webapp2.RequestHandler):
    def get(self):
        

        user = users.get_current_user()
        if user == None: #if they are not logged in 
            self.redirect("/homepage")
            return
        user = newuser.UserModel.query(newuser.UserModel.user_email == user.email()).get()
        if user != None: #asks python if the user signed in currently already has an account
            self.redirect("/find")
            return

        template = jinja_env.env.get_template('templates/signup.html')

        self.response.out.write(template.render(output))

        #connecting the response from multiple choice with a value
    def post(self):
        user = users.get_current_user()
        if user == None:
            self.redirect("/homepage")
            return
        r_clean = self.request.get("form_clean")
        r_week = self.request.get("form_week")
        r_weeknd = self.request.get("form_weeknd")
        

        new_user = newuser.UserModel(clenliness = r_clean, weekwake = r_week,
         weekndwake = r_weeknd, user_email = user.email())
        new_user.put()
        self.redirect("/find")








        