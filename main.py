import os
import webapp2

from handlers import jinja_env
from handlers import main_handler
from handlers import signup_handler

jinja_env.init(os.path.dirname(__file__))

app = webapp2.WSGIApplication([
    ('/homepage', main_handler.MainHandler),
    ('/signup', signup_handler.SignUpHandler),
], debug=True)
