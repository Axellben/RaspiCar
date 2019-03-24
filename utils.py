import sys
import time
import RPi.GPIO as GPIO

class CAR:

  def __init__(self, forward_pin=21, backward_pin=20, sleeptime=0.1):
    self.f_pin = forward_pin
    self.b_pin = backward_pin
    self.sleeptime = sleeptime

    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.f_pin, GPIO.OUT)
    GPIO.setup(self.b_pin, GPIO.OUT)

  def forward(self):
    GPIO.output(self.f_pin, GPIO.HIGH)
    time.sleep(self.sleeptime)
    GPIO.output(self.f_pin, GPIO.LOW)

  def backward(self):
    GPIO.output(self.b_pin, GPIO.HIGH)
    time.sleep(self.sleeptime)
    GPIO.output(self.b_pin, GPIO.LOW)
