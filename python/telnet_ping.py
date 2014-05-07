#!/usr/bin/env python

import socket
from telnetlib import Telnet

def can_reach(host, port, timeout=5):
    try:
        tn = Telnet(host, port, timeout)
        return 0 # successful posix status
    except socket.error, e:
        return e.errno

if __name__ == '__main__':
    import argparse
    import sys
    parser = argparse.ArgumentParser('Telnet Ping')
    parser.add_argument('host')
    parser.add_argument('port')
    parser.add_argument('-t', dest='timeout', default=5)
    options = parser.parse_args()
    result = can_reach(options.host, options.port, options.timeout)
    sys.exit(result)
