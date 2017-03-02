'''
Created on 04 Nov 2014

@author: debrouk
'''

from threading import Thread
import RPi.GPIO as GPIO
import time
import os

class myListenThread(Thread):
    def __init__(self):
        ''' Constructor. '''
        Thread.__init__(self)
        self.buttonPressed=None
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(2,GPIO.IN)
        GPIO.setup(3,GPIO.IN)
        GPIO.setup(4,GPIO.IN,pull_up_down = GPIO.PUD_UP)
        print("Thread created")
        pass
    
    def run(self):
        """ this function will be running to listen to the buttons input
        currently just listening for a 1 keypress
        """
        #inputFromUser = input("Duw eens op 1:")
        #if inputFromUser=="1":
        #    self.buttonPressed=True
        #    return
        print ("the thread is now running")
        while True:
            if (GPIO.input(2)) == 0:
                self.buttonPressed = 'red'
                #os.system('mpg321 buzzer.mp3 &')
                print('red')
                return
            elif (GPIO.input(3)) == 0:
                self.buttonPressed = 'green'
                #os.system('mpg321 buzzer.mp3 &')
                print('green')
                return
            elif (GPIO.input(4)) == 0:
                self.buttonPressed = 'blue'
                #os.system('mpg321 buzzer.mp3 &')
                print('yellow')
                return

        
                
