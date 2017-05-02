#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

ulimit -c unlimited
echo 1 > /proc/sys/fs/suid_dumpable

cat /proc/sys/kernel/core_pattern
