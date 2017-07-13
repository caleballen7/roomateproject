
import jinja_env
import logging
import webapp2



class FindHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("findHandler")
        # do stuff with books...
        html_params = {
            "title": "Second Title",
            "content": "Some stuff about books."
        }
        template = jinja_env.env.get_template('templates/findaroomate.html')
        self.response.out.write(template.render(html_params))