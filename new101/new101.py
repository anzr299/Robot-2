import time
import serial

ser = serial.Serial("/dev/ttyACM0" ,9600)

ser.write('s'.encode())
