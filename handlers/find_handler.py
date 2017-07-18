
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

        matchedRoommates = newuser.UserModel.query().fetch()
        for match in matchedRoommates:
            score = 0
            if match.clenliness == myUser.clenliness:
                score = score + 1
            if match.weekwake == myUser.weekwake:
                score = score + 1
            if match.weekndwake == myUser.weekndwake:
                score = score + 1

            match.score = score 


        match_str = ""
        for match in matchedRoommates:
            match_str += "<div> Compatibility Score: " + str(match.score) + "<br>" + "<b>" + str(match.form_first) + " " + str(match.form_last) + ", " + str(match.age) + "</b>"
            match_str+= "<p>" + "Dorm: " + str(match.dorm) + "<br>"
            match_str += "Bio: " + str(match.form_bio)+ "<br>"
            match_str += "Email: " + str(match.user_email) + "<br>"
            if match.insta != None: 
                match_str += "<a href = http://www.instagram.com/" + str(match.insta) + "> Instagram </a>"
            if match.twitter!= None:
                match_str += "<a href = http://www.twitter.com/" + str(match.twitter) + "> Twitter </a>"
            match_str+= "</div>"

        template = jinja_env.env.get_template('templates/find.html')
        parajo = {
            "html_userObject": match_str,
            "html_info": new_user,
            "html_email" : user.email()
            }

        self.response.out.write(template.render(parajo))
