import cherrypy

import os

HTML = """<html>
          <head></head>
          <body>
            <form method="get" action="start">
              {button}
              <button type="submit">Start</button>
            </form>
            <form method="get" action="{actionForRed}">
              <button type="submit">Toggle red LED</button>
            </form>
          </body>
        </html>"""


class Quiz(object):
    def __init__(self):
        self.buttonRed = """<img src="/static/buttonRed.jpg" height="100" width="100">"""
        self.buttonGreen = """<img src="/static/buttonGreen.png" height="100" width="100">"""
        self.buttonGrey = """<img src="/static/buttonGrey.jpg" height="100" width="100">"""

    @cherrypy.expose
    def index(self):
        return HTML.format(button=self.buttonRed,actionForRed="ternRedOn")
