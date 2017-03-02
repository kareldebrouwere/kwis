import cherrypy

import os

HTML = """<html>
          <head></head>
          <body>
            {button1}
            {button2}
            {button3}
        </body>
        </html>"""


class Quiz(object):
    def __init__(self):
        self.buttonRed = """<img src="/static/buttonRed.jpg" height="100" width="100">"""
        self.buttonBlue = """<img src="/static/buttonBlue.png" height="100" width="100">"""
        self.buttonGrey = """<img src="/static/buttonGrey.jpg" height="100" width="100">"""

    @cherrypy.expose
    def index(self):
        return HTML.format(button1=self.buttonRed,button2=self.buttonBlue,button3=self.buttonGrey)


if __name__ == "__main__":
    config = os.path.join(os.path.dirname(__file__),'cherrypy.conf')
    cherrypy.quickstart(Quiz(),config = config)