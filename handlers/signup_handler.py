
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
            self.redirect(users.create_login_url('/signup'))
            return
        user = newuser.UserModel.query(newuser.UserModel.user_email == user.email()).get()
        if user != None: #asks python if the user signed in currently already has an account
            self.redirect("/find")
            return

        template = jinja_env.env.get_template('templates/signup.html')

        self.response.out.write(template.render())

        #connecting the response from multiple choice with a value
    def post(self):
        user = users.get_current_user()
        if user == None:
            self.redirect("/homepage")
            return
        r_clean = self.request.get("form_clean")
        r_week = self.request.get("form_week")
        r_weeknd = self.request.get("form_weeknd")
        r_bio = self.request.get("form_bio")
        r_last = self.request.get("form_last")
        r_first = self.request.get("form_first")
        r_dorm = self.request.get("dorm")
        r_gradyear = self.request.get("gradyear")
        r_age = self.request.get("age")
        r_insta = self.request.get("insta")
        r_score = self.request.get("score")
        r_twitter = self.request.get("twitter")


        new_user = newuser.UserModel(clenliness = r_clean,
        weekwake = r_week,
        weekndwake = r_weeknd, 
        user_email = user.email(),
        form_first = r_first,
        form_last = r_last,
        form_bio = r_bio,
        dorm = r_dorm,
        gradyear = r_gradyear,
        age = r_age,
        insta = r_insta,
        twitter = r_twitter




        )
        new_user.put()
        self.redirect("/find")








        