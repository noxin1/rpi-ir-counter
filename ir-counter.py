import RPi.GPIO as GPIO
import pyfiglet
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
COUNT=0
LAST=1
print(pyfiglet.figlet_format(str(COUNT)),end="\r")

while True:
    sensor=GPIO.input(17)
    if sensor==0:
       if sensor != LAST:
        COUNT+=1
        print('\a')
        print(pyfiglet.figlet_format(str(COUNT)),end="\r")
    LAST=sensor
    sleep(0.02)
