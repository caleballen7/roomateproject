import os
import webapp2

from handlers import jinja_env
from handlers import main_handler
from handlers import book_handler

jinja_env.init(os.path.dirname(__file__))

app = webapp2.WSGIApplication([
    ('/', main_handler.MainHandler),
    ('/books', book_handler.BookHandler),
], debug=True)
