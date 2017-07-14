
import jinja_env
import logging
import webapp2



class HomepageHandler(webapp2.RequestHandler):
    def get(self):
    	logging.info("SecondHandler")
    	
        html_params = {
        }
        template = jinja_env.env.get_template('templates/homepage.html')
        self.response.out.write(template.render(html_params))