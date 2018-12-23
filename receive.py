#!/usr/bin/python

import sys
import serial


if len(sys.argv) < 1:
    print("Missing port")
    exit()

port = sys.argv[1].split(':')
if len(port) > 1:
    speed = int(port[1])
else:
    speed = 115200
port = port[0]
print("Waiting for incoming characters on port " + port + " at speed " + str(speed) + " bauds.")

ser = serial.Serial(port=port, baudrate=speed)

while True:
    print(ord(ser.read()), sep='')
