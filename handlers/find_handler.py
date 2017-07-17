
import jinja_env
import logging
import webapp2
from google.appengine.api import users
from models import newuser


class FindHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user == None:
            self.redirect("/homepage")
            return
        user = newuser.UserModel.query(newuser.UserModel.user_email == user.email()).get()
        new_user = "<p>" + "You are " + str(user.clenliness) + " clean. You wake up around " + str(user.weekwake) + " during the week, and " + str(user.weekndwake) + " on the weekends. Here are people that you would be good roommates with!"

        user_params = {
            "html_info": new_user,
            }
        
        #connecting the response from multiple choice with a value
        template = jinja_env.env.get_template('templates/find.html')
        self.response.out.write(template.render(user_params))