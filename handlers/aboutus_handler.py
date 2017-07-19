import jinja_env
import logging
import webapp2

class AboutUsHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("aboutushandler")


        template = jinja_env.env.get_template('templates/aboutus.html')