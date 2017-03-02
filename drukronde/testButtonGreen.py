import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if (GPIO.input(17)) == 0:
        buttonPressed = 'red'
        # os.system('mpg321 buzzer.mp3 &')
        print('red')
    elif (GPIO.input(18)) == 0:
        buttonPressed = 'green'
        # os.system('mpg321 buzzer.mp3 &')
        print('green')
    elif (GPIO.input(21)) == 0:
        buttonPressed = 'yellow'
        # os.system('mpg321 buzzer.mp3 &')
        print('yellow')