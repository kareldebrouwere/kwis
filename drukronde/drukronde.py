'''
Created on 19-nov.-2014

@author: karel
'''

from tkinter import Tk,Frame,Canvas,Button
from myListenThread import myListenThread


class drukKnopRonde(Tk):
    '''
    Application that shows 3 colors animated, and will hightlight the one who first pressed the button
    needs to work with the myListenThread to get the button input
    '''
    def __init__(self):
        hd_hor=300
        hd_vert = 300
        box_size = 40
        space_between=(hd_hor - (box_size*3))/4
        Tk.__init__(self)
        self.geometry("600x700")
        self.title('drukken')
        self.controlFr = Frame(self,bg='yellow')
        self.controlFr.pack(side = 'bottom')
        self.canvas = Canvas(self,height=300,width=300,bg='blue')
        self.canvas.pack(side='top',fill='y')
        self.xred1=space_between
        self.y1=(hd_vert/2)-(box_size/2)
        self.y2=self.y1+box_size
        self.xred2=space_between+box_size
        self.xgreen1 = box_size+(space_between*2)
        self.xgreen2 = self.xgreen1 + box_size
        self.xyellow1 = (box_size*2) + (space_between*3)
        self.xyellow2 = self.xyellow1 + box_size
        self.canvas.pack()
        self.variant = int('0x10',16)
        self.updown = 'up'
        self.startButton = Button(self,text="Start",command = lambda: self.startQuestion())
        self.startButton.pack()
        self.redboxid=0
   
    def startQuestion(self):
        self.startButton.pack_forget()
        self.drawStartBoxes()
        self.listenThread = myListenThread()
        self.listenThread.start()    
        self.waitForAnswers()
        self.startButton.pack()

    def drawStartBoxes(self):
        if self.redboxid != 0:
            print('redboxid = '+str(self.redboxid)+' has been deleted')
            self.canvas.delete(self.redboxid)
        print('next line draws red box')
        self.redboxid = self.canvas.create_rectangle(self.xred1,self.y1,self.xred2,self.y2,fill="red")
        
        print('x1='+str(self.xred1)+'    y1='+str(self.y1)+'     x2='+str(self.xred2)+'     y2='+str(self.y2)+'     boxid='+str(self.redboxid))
        self.canvas.create_rectangle(self.xgreen1,self.y1,self.xgreen2,self.y2,fill="green")
        self.canvas.create_rectangle(self.xyellow1,self.y1,self.xyellow2,self.y2,fill="yellow")
        self.canvas.update_idletasks()

        
    def waitForAnswers(self):
       
        while self.listenThread.buttonPressed==  'none':
            #print('no button pressed')
            temp=0

        if self.listenThread.buttonPressed == "red":
           
            self.redboxid = self.canvas.create_rectangle(self.xred1,self.y1,self.xred2,self.y2,fill="red")
            print('x1='+str(self.xred1)+'    y1='+str(self.y1)+'     x2='+str(self.xred2)+'     y2='+str(self.y2)+'     boxid='+str(self.redboxid))
            self.greenboxid = self.canvas.create_rectangle(self.xgreen1,self.y1,self.xgreen2,self.y2,fill="grey")
            
            self.yellowboxid = self.canvas.create_rectangle(self.xyellow1,self.y1,self.xyellow2,self.y2,fill="grey")
            self.canvas.pack()
            self.listenThread.buttonPressed = "none"
            return
        elif self.listenThread.buttonPressed == "green":
            
            self.redboxid = self.canvas.create_rectangle(self.xred1,self.y1,self.xred2,self.y2,fill="grey")
            print('x1='+str(self.xred1)+'    y1='+str(self.y1)+'     x2='+str(self.xred2)+'     y2='+str(self.y2)+'     boxid='+str(self.redboxid))
            self.greenboxid = self.canvas.create_rectangle(self.xgreen1,self.y1,self.xgreen2,self.y2,fill="green")
          
            self.yellowboxid = self.canvas.create_rectangle(self.xyellow1,self.y1,self.xyellow2,self.y2,fill="grey")
            self.canvas.pack()
            self.listenThread.buttonPressed = "none"
            return
        elif self.listenThread.buttonPressed == "yellow":
           
            self.redboxid = self.canvas.create_rectangle(self.xred1,self.y1,self.xred2,self.y2,fill="grey")
            print('x1='+str(self.xred1)+'    y1='+str(self.y1)+'     x2='+str(self.xred2)+'     y2='+str(self.y2)+'     boxid='+str(self.redboxid))
            self.greenboxid = self.canvas.create_rectangle(self.xgreen1,self.y1,self.xgreen2,self.y2,fill="grey")
          
            self.yellowboxid = self.canvas.create_rectangle(self.xyellow1,self.y1,self.xyellow2,self.y2,fill="yellow")
            self.canvas.pack()
            self.listenThread.buttonPressed = "none"
            return
    
        
               
        
    
    


if __name__ == "__main__":        
    app = drukKnopRonde()
    app.mainloop()


    
