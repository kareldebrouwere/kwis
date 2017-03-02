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
        self.HTML = """<html>
                  <head></head>
                  <body>
                    <form>
                      {pushbutton1}
                      {pushbutton2}
                      {pushbutton3}
                    </form>
                    <form>
                      {action}
                    </form>
                </body>
                </html>"""

        self.buttonRed = """<img src="/static/buttonRed.jpg" height="100" width="100">"""
        self.buttonBlue = """<img src="/static/buttonBlue.jpg" height="100" width="100">"""
        self.buttonGrey = """<img src="/static/buttonGrey.jpg" height="100" width="100">"""
        self.buttonGreen = """<img src="/static/buttonGreen.png" height="100" width="100">"""
        self.action = """<form method="get" action="displayRed">
            <button type="submit">Start</button>
            </form>
            """
        self.pageHTML = self.HTML.format(pushbutton1=self.buttonGrey, pushbutton2=self.buttonGrey, pushbutton3=self.buttonGrey, action=self.action)

    @cherrypy.expose
    def index(self):
        return self.pageHTML

    @cherrypy.expose
    def displayRed(self):
        print ("In the red button loop")
        self.pageHTML = self.HTML.format(pushbutton1=self.buttonRed,pushbutton2=self.buttonGrey,pushbutton3=self.buttonGrey,action="self.action")
        self.index()

    @cherrypy.expose
    def displayBlue(self):
        return HTML.format(pushbutton1=self.buttonGrey, pushbutton2=self.buttonBlue, pushbutton3=self.buttonGrey)

    @cherrypy.expose
    def displayGeen(self):
        return HTML.format(pushbutton1=self.buttonGrey, pushbutton2=self.buttonGrey, pushbutton3=self.buttonGreen)


if __name__ == "__main__":
    config = os.path.join(os.path.dirname(__file__),'cherrypy.conf')
    cherrypy.quickstart(Quiz(),config = config)