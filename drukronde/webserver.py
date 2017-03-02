import cherrypy

import os

HTML = """<html>
          <head></head>
          <body>
            <form>
             {button1}
             {button2}
             {button3}
            </form>
            <form>
             {action}
            </form>
        </body>
        </html>"""


class Quiz(object):
    def __init__(self):
        self.buttonRed = """<img src="/static/buttonRed.jpg" height="100" width="100">"""
        self.buttonBlue = """<img src="/static/buttonBlue.jpg" height="100" width="100">"""
        self.buttonGrey = """<img src="/static/buttonGrey.jpg" height="100" width="100">"""
        self.buttonGreen = """<img src="/static/buttonGreen.png" height="100" width="100">"""
        self.action = """method="get" action="{actionForRed}">\n<button type="submit">Toggle red LED</button>"""

    @cherrypy.expose
    def index(self):
        return HTML.format(button1=self.buttonGrey,button2=self.buttonGrey,button3=self.buttonGrey,action=self.action)

    @cherrypy.expose
    def displayRed(self):
        return HTML.format(button1=self.buttonRed,button2=self.buttonGrey,button3=self.buttonGrey)

    @cherrypy.expose
    def displayBlue(self):
        return HTML.format(button1=self.buttonGrey, button2=self.buttonBlue, button3=self.buttonGrey)

    @cherrypy.expose
    def displayGeen(self):
        return HTML.format(button1=self.buttonGrey, button2=self.buttonGrey, button3=self.buttonGreen)


if __name__ == "__main__":
    config = os.path.join(os.path.dirname(__file__),'cherrypy.conf')
    cherrypy.quickstart(Quiz(),config = config)