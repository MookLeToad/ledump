"""
cloudflare-static/email-decode.min.js
arg = "06516f686269717546646969727572677228626772"
"""

from sys import argv

def decrapt(arg):
  return ''.join([chr(int(arg[x:x+2], 16) ^ int(arg[0:2], 16) if x!= 0 else int(arg[x:x+2], 16)) for x in range(0,len(arg),2)][1:])

def encrapt(message, xorByte):
  return ''.join(["%0.2X" % xorByte] + ["%0.2X" % (ord(c) ^ xorByte) for c in message])

if argv[1]=="e":
  print(encrapt(argv[2],int(argv[3])))
if argv[1]=="d":
  print(decrapt(argv[2]))
