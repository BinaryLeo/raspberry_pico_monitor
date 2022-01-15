import sys
import re  # regular expression
import serial
from serial.tools import list_ports
#------------------------------------- // Import dependencies

myPorts = serial.tools.list_ports.comports()
ListPorts = []  # An empty list to receive our available COM Ports

for p in myPorts:
  ListPorts.append(p.device)  # Append Port
print(len(myPorts), 'ports found') # List the number of ports
print(ListPorts)  # Print the available ports

# Serial takes two parameters: serial device and baudrate
port = input("Type a COM port: ").upper()

if port[-1].isdigit:
 port = "COM" + port
print(port)
if port in ListPorts:
    print(port + " is available to read data, plz continue and ...")
    baud_rate = input("Type the Baud Rate: ")
    if baud_rate.isalnum(): # Baudratevalidator
        print("Baudrate invalid ... new baudrade: 115200")
        baud_rate =115200
    ser = serial.Serial("{}".format(port), baud_rate)
   
    if(ser.isOpen()):
      print("This port is alredy open")
      while True:
        data = ser.readline()
        data = data.replace(b'\n', b'').replace(b'\r', b'')  # format string
        print(str(data, 'utf-8'))  # utf-8 string
else:
    print("Check the available ports and try again")
    print(ListPorts)





