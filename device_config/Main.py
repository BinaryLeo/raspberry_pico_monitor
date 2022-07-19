from machine import Pin
import time
import utime

led = Pin(25, Pin.OUT)
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)
 
while True:
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = 27 - (reading - 0.706)/0.001721
    print ("{0:.1f}".format(temperature)) 
    utime.sleep(2)
    if temperature >= 27:
        print(u"\U0001F525","Temp. above the normal range")
        led.value(1)
        time.sleep(1)
        led.value(0)
        time.sleep(1)
    else:
         led.value(0)
         time.sleep(0)
