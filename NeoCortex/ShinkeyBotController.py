import numpy as np
import cv2

import socket
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#server_address = ('192.168.0.110', 10001)
#server_address = ('10.16.23.142', 10001)

print sys.argv

if (len(sys.argv)<2):
    ip = '192.168.0.110'
else:
    ip = sys.argv[1]


server_address = (ip, 10001)

myip = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1]

myip = myip[0]

data1 = int(myip.split('.')[0])
data2 = int(myip.split('.')[1])
data3 = int(myip.split('.')[2])
data4 = int(myip.split('.')[3])

print str(data1)+'.'+str(data2)+'.'+str(data3)+'.'+str(data4)



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
      data = int(myip.split('.')[0])
      sent = sock.sendto(data, server_address)


  if (data.startswith('X')):
      break
      
sock.close()
