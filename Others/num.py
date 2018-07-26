#!/usr/bin/env python
# coding=utf-8

import random
rand_num = random.randrange(10)

for i in range(3):
    guss_num = int(raw_input("number?"))
    if guss_num == rand_num:
        print "success"
        break
    elif guss_num > rand_num:
        print "large"
    else:
        print "small"
else:
        print "failed"

print "real num is: %s" %rand_num