
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

        matchedRoommates = [
        newuser.UserModel(form_first= "Lauren ", form_last = "Fraser" ,
        dorm = "Frazier Hall" , user_email = "laurenf@mail.com", user_bio = "I am lauren and I like ice cream. ", age = "18", insta = "instagram.com/laurenpfraser"),
        newuser.UserModel(clenliness = "not", weekwake = "8am",
         weekndwake ="9am", user_email = "kaurenp@mail.com"), 
        newuser.UserModel(clenliness = "somewhat", weekwake = "6am",
         weekndwake ="10am", user_email = "maurenf@mail.com"), 
        ]

        match_str = ""
        for match in matchedRoommates:
            match_str += "<div>" + "<b>" + str(match.form_first) + " " + str(match.form_last) + ", " + str(match.age) + "</b>"
            match_str+= "<p>" + "Dorm: " + str(match.dorm) + "<br>"
            match_str += "Bio: " + str(match.user_bio)+ "<br>"
            match_str += "Email: " + str(match.user_email) + "<br>"
            match_str += "<a href = " + str(match.insta) + "> Instagram </a>" + "</div>"

        template = jinja_env.env.get_template('templates/find.html')
        parajo = {
            "html_userObject": match_str,
            "html_info": new_user,
            "html_email" : user.email()
            }

        self.response.out.write(template.render(parajo))
