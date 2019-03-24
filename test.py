import sys
import time
import RPi.GPIO as GPIO

Forward=21
Backward=20
sleeptime=1

GPIO.cleanup()

GPIO.setmode(GPIO.BCM) 
#:wqGPIO.setmode(GPIO.BOARD)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)

def forward(x):
    GPIO.output(Forward, GPIO.HIGH)
    print("Moving Forward")
    time.sleep(x)
    GPIO.output(Forward, GPIO.LOW)

def reverse(x):
    GPIO.output(Backward, GPIO.HIGH)
    print("Moving Backward")
    time.sleep(x)
    GPIO.output(Backward, GPIO.LOW)

while (1):

    forward(5)
    reverse(5)
    GPIO.cleanup()
