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
        self.buttonPressed='none'
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17,GPIO.IN,pull_up_down = GPIO.PUD_UP)
        GPIO.setup(18,GPIO.IN,pull_up_down = GPIO.PUD_UP)
        GPIO.setup(21,GPIO.IN,pull_up_down = GPIO.PUD_UP)
        pass
    
    def run(self):
        """ this function will be running to listen to the buttons input
        currently just listening for a 1 keypress
        """
        #inputFromUser = input("Duw eens op 1:")
        #if inputFromUser=="1":
        #    self.buttonPressed=True
        #    return

        while True:
            if (GPIO.input(17)) == 0:
                self.buttonPressed = 'red'
                #os.system('mpg321 buzzer.mp3 &')
                print('red')
                return
            elif (GPIO.input(18)) == 0:
                self.buttonPressed = 'green'
                #os.system('mpg321 buzzer.mp3 &')
                print('green')
                return
            elif (GPIO.input(21)) == 0:
                self.buttonPressed = 'yellow'
                #os.system('mpg321 buzzer.mp3 &')
                print('yellow')
                return
            
        
                
