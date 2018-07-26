#!/usr/bin/env python
# coding=utf-8

def count():
    name = "melody"
    for i in range(1,10):
        if i == 5:
            print "wow"
        else:
            print i
    return name

user=count()
if user=="melody":
    print "this is your turn melody"
