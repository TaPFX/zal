#OSC server um ein Zeichen ans Licht zu geben

import argparse
import math
import socket
import time

import RPi.GPIO as GPIO

from pythonosc import dispatcher
from pythonosc import osc_server

statusPin = 11
relayPin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(relayPin, GPIO.OUT)
GPIO.setup(statusPin, GPIO.OUT)

def get_ip_address():
 ip_address = '';
 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 s.connect(("8.8.8.8",80))
 ip_address = s.getsockname()[0]
 s.close()
 return ip_address

def zal_handler(unused_addr, args):
  print("Zeichen an Licht, T-10 Sekunden")
  GPIO.output(relayPin, GPIO.HIGH)
  time.sleep(1)
  GPIO.output(relayPin, GPIO.LOW)
  #Set GPI Pin 10 to ON for 1 sec to switch the Relay

if __name__ == "__main__":
  local_ip = get_ip_address()
  print(local_ip)
  
  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/zal", zal_handler)

  server = osc_server.ThreadingOSCUDPServer((local_ip, 50005), dispatcher)
  print("Serving on {}".format(server.server_address))
  GPIO.output(statusPin, GPIO.HIGH)
  server.serve_forever()
