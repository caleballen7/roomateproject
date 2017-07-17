import os
import webapp2
import logging

from handlers import jinja_env
from handlers import main_handler
from handlers import signup_handler
from handlers import homepage_handler
from handlers import find_handler

jinja_env.init(os.path.dirname(__file__))

app = webapp2.WSGIApplication([
    ('/homepage', homepage_handler.HomepageHandler),
    ('/signup', signup_handler.SignUpHandler),
    ('/find', find_handler.FindHandler),
], debug=True)
