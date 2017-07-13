
import jinja_env
import logging
import webapp2



class SignUpHandler(webapp2.RequestHandler):
    def get(self):
    	logging.info("SecondHandler")
    	# do stuff with books...
        html_params = {
        }
        template = jinja_env.env.get_template('templates/signup.html')
        self.response.out.write(template.render(html_params))