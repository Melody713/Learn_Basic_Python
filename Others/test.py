#!/usr/bin/env python
# coding=utf-8

import sys
import getpass

print sys.argv

name = raw_input("user:")
pwd = getpass.getpass("pwd:")

if name == "melody" and pwd == "123":
    print "success"
else:
    print "failed"