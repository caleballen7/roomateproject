
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
        myUser = newuser.UserModel.query(newuser.UserModel.user_email == user.email()).get()
        new_user = "<div>" + "You are " + str(myUser.clenliness) + " clean. You wake up around " + str(myUser.weekwake) + " during the week, and " + str(myUser.weekndwake) + " on the weekends. Here are people that you would be good roommates with!" + "</div>"

        user_params = {
            "html_info": new_user,
            "html_email" : user.email()
            }
        matchedRoommates = [
        newuser.UserModel(clenliness = "very", weekwake = "7am",
         weekndwake ="9am", user_email = "laurenf@mail.com"), 
        newuser.UserModel(clenliness = "not", weekwake = "8am",
         weekndwake ="9am", user_email = "kaurenp@mail.com"), 
        newuser.UserModel(clenliness = "somewhat", weekwake = "6am",
         weekndwake ="10am", user_email = "maurenf@mail.com"), 
        ]

        match_str = ""
        for match in matchedRoommates:
            match_str += "<h3>" + str(match.clenliness) + str(match.weekndwake) + str(match.weekwake) + ", " + str(match.user_email) + "</h3>"
        template = jinja_env.env.get_template('templates/find.html')
        parajo = {
            "html_userObject": match_str,
            }

        
        self.response.out.write(template.render(parajo))
