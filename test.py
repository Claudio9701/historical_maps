import serial
import time

with serial.Serial('/dev/ttyACM0', 9600, timeout=1) as ser:
    while True:
        
        time.sleep(1)
        