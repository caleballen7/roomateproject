
class HomePageHandler(webapp2.RequestHandler):
    def get(self):
    	logging.info("SecondHandler")
..
        html_params = {
            "title": "Second Title",
            "content": "Some stuff about books."
        }
        template = jinja_env.env.get_template('templates/homepage.html')
        self.response.out.write(template.render(html_params))