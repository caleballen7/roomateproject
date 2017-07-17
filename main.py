import os
import webapp2

from handlers import jinja_env
from handlers import main_handler
from handlers import signup_handler
from handlers import login_handler
from handlers import homepage_handler

jinja_env.init(os.path.dirname(__file__))


app = webapp2.WSGIApplication([
    ('/homepage', homepage_handler.HomepageHandler),
    ('/signup', signup_handler.SignUpHandler),
    ('/login', login_handler.LoginHandler),
], debug=True)
