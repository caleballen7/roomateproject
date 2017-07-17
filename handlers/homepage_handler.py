
import jinja_env
import logging
import webapp2
from google.appengine.api import users




class HomepageHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("SecondHandler")
        
        homepagedic = {

          "html_login_url": users.create_login_url('/signup'),

        }
        template = jinja_env.env.get_template('templates/homepage.html')










        self.response.out.write(template.render(homepagedic))