from machine import Pin
import time

led = Pin("LED", Pin.OUT)
duration = int(input("Enter duration: "))

for i in range(5):
    led.value(1)
    time.sleep(duration)
    led.value(0)
    time.sleep(1)
    

