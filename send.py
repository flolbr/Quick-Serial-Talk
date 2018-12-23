#!/usr/bin/python

import sys
import serial

if len(sys.argv) < 1:
    print("Missing port")
    exit()
elif len(sys.argv) < 2:
    print("Missing characters to send")
    exit()

port = sys.argv[1].split(':')

if len(port) > 1:
    speed = int(port[1])
else:
    speed = 115200
port = port[0]
print("Sending characters to port " + port + " at speed " + str(speed) + " bauds.")

ser = serial.Serial(port=port, baudrate=speed)

[ser.write(str.encode(chr(int(char)))) for char in sys.argv[2:]]
