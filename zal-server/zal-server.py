#OSC server um ein Zeichen ans Licht zu geben

import argparse
import math
import netifaces

from pythonosc import dispatcher
from pythonosc import osc_server

def zal_handler(unused_addr, args):
  print("Zeichen an Licht, T-10 Sekunden")
  #Set GPI Pin 10 to ON for 1 sec to switch the Relay



if __name__ == "__main__":
  hostname = socket.gethostname()
  local_ip = socket.gethostbyname(hostname)
  print(hostname, local_ip)
  
  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/zal", zal_handler)

  server = osc_server.ThreadingOSCUDPServer((local_ip, 50005), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()
