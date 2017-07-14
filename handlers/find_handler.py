
import jinja_env
import logging
import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb


class FindHandler(webapp2.RequestHandler):
    def get(self):
        # do stuff with books...
        html_params = {
            "title": "Second Title",
            "content": "Some stuff about books."
        }
        template = jinja_env.env.get_template('templates/find.html')
        self.response.out.write(template.render(html_params))