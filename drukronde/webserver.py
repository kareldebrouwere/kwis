import os

import cherrypy

from drukronde import myListenThread as myListenThread

import time

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
                  <head>Kwis Web Application</head>
                  <body>
                    <form>
                      {pushbutton1}
                      {pushbutton2}
                      {pushbutton3}
                    </form>
                    {action}
                </body>
                </html>"""

        self.buttonRed = """<img src="/static/buttonRed.jpg" height="100" width="100">"""
        self.buttonBlue = """<img src="/static/buttonBlue.jpg" height="100" width="100">"""
        self.buttonGrey = """<img src="/static/buttonGrey.jpg" height="100" width="100">"""
        self.buttonGreen = """<img src="/static/buttonGreen.png" height="100" width="100">"""
        self.actionStart = """<form method="get" action="start">
                            <button type="submit">Start</button>
                            </form>
                    """
        self.actionReset = """<form method="get" action="index">
                                   <button type="submit">Reset</button>
                                   </form>
                           """



    @cherrypy.expose
    def index(self):
        print("running the index method")
        self.pageHTML = self.HTML.format(pushbutton1=self.buttonGrey, pushbutton2=self.buttonGrey,
                                         pushbutton3=self.buttonGrey, action=self.actionStart)
        return self.pageHTML

    @cherrypy.expose
    def start(self):
        newListenThread= myListenThread()
        while newListenThread.buttonPressed==None:
            #print("nothing happens")
            time.sleep(1)
        print ("ButtonPressed!!!" + newListenThread.buttonPressed)


    @cherrypy.expose
    def displayRed(self):
        print ("In the red button loop")
        self.pageHTML = self.HTML.format(pushbutton1=self.buttonRed,pushbutton2=self.buttonGrey,pushbutton3=self.buttonGrey,action=self.actionReset)
        return self.pageHTML

    @cherrypy.expose
    def displayBlue(self):
        return HTML.format(pushbutton1=self.buttonGrey, pushbutton2=self.buttonBlue, pushbutton3=self.buttonGrey)

    @cherrypy.expose
    def displayGeen(self):
        return HTML.format(pushbutton1=self.buttonGrey, pushbutton2=self.buttonGrey, pushbutton3=self.buttonGreen)


if __name__ == "__main__":
    config = os.path.join(os.path.dirname(__file__),'cherrypy.conf')
    cherrypy.quickstart(Quiz(),config = config)