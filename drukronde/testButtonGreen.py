import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if (GPIO.input(2)) == 0:
        buttonPressed = 'red'
        # os.system('mpg321 buzzer.mp3 &')
        print('red')
    elif (GPIO.input(3)) == 0:
        buttonPressed = 'green'
        # os.system('mpg321 buzzer.mp3 &')
        print('green')
    elif (GPIO.input(4)) == 0:
        buttonPressed = 'yellow'
        # os.system('mpg321 buzzer.mp3 &')
        print('yellow')