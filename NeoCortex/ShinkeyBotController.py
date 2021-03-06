#coding: latin-1
import numpy as np
import cv2

import socket
import sys

import time

import MCast


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#server_address = ('192.168.0.110', 10001)
#server_address = ('10.16.23.142', 10001)

# Fetch the remote ip if I do not have one.  It should be multicasted by ShinkeyBot
reporter = MCast.Receiver()

print sys.argv

if (len(sys.argv)<2):
    print "Waiting for Multicast Message"
    shinkeybotip = reporter.receive()
    print 'ShinkeyBot IP:' + shinkeybotip
    ip = shinkeybotip
elif sys.argv[1] == '-f':
    print "Forcing IP Address"
    ip = '192.168.0.110'
else:
    ip = sys.argv[1]
    print "Using IP:"+ip

server_address = (ip, 10001)

def _find_getch():
    try:
        import termios
    except ImportError:
        # Non-POSIX. Return msvcrt's (Windows') getch.
        import msvcrt
        return msvcrt.getch

    # POSIX system. Create and return a getch that manipulates the tty.
    import sys, tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    return _getch

getch = _find_getch()

while (True):
  print '>'
  data = getch()

  sent = sock.sendto(data, server_address)

  if (data.startswith('!')):
      print "Letting know ShinkeyBot that I want streaming...."

  if (data.startswith('X')):
      break

sock.close()
