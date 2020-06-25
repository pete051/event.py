#!/usr/bin/env python
import time
import RPI.GPIO as GPIO

def buttonEventHandler(pin):
    print("handling button event")
    GPIO.output(25,True)
    time.sleep(0.5)
    GPIO.output(25,False)

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23,GPIO.IN)
    GPIO.setup(24,GPIO.OUT)
    GPIO.setup(25,GPIO.OUT)

    GPIO.add_event_detect(23,GPIO.FALLING)
    GPIO.add_event_callback(23,buttonEventHandler,100)

    GPIO.output(25,False)
    GPIO.output(24,True)

    p=0.
    while True:
        p^=True
        GPIO.output(24,p)
        time.sleep(0.5)

GPIO.cleanup()

if __name__=="__main__":
    main()



    
