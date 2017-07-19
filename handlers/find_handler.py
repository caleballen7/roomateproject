
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
            if match.dorm == myUser.dorm:
                score = score +20
            if match.gradyear == myUser.gradyear:
                score = score + 10
            if match.age == myUser.age:
                score = score + 3
            if match.friends == myUser.friends:
                score = score + 1
            if match.noiselevel == myUser.noiselevel:
                score = score + 1
            if match.bed == myUser.bed:
                score = score + 1
            if match.God == myUser.God:
                score = score + 1
            if match.hotorcold == myUser.hotorcold:
                score = score + 1
            if match.study == myUser.study:
                score = score + 1 
            if match.sex == myUser.sex:
                score = score + 100
            if match.sports == myUser.sports:
                score = score + 1
            if match.reading == myUser.reading:
                score = score + 1
            if match.game == myUser.game:
                score = score + 1
            if match.netflix == myUser.netflix:
                score = score + 1
            if match.tech == myUser.tech:
                score = score + 1





            match.score = score 
##This sorts the users from highest compatability to lowest
        matchedRoommates.sort(key=lambda roommate: roommate.score, reverse = True)
##This takes out the user trying to find a roommate from the list of options
        matchedRoommates= matchedRoommates[1:]


        match_str = ""
        for match in matchedRoommates:
            match_str += "<div> Compatibility Score: " + str(match.score) + "<br>" + "<b>" + str(match.form_first) + " " + str(match.form_last) + ", " + str(match.age) + "</b>"
            match_str+= "<br><b>" + "Dorm: </b>" + str(match.dorm) + "<br>"
            match_str += "<b>Bio:</b> " + str(match.form_bio)+ "<br>"
            match_str += "<b> Pet Peeves: </b>" + str(match.petpeeves) + "<br>"
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
