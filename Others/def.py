#!/usr/bin/env python
# coding=utf-8
def count():
    for i in range(1,10):
        if i==5:
            return
        else:
            print i
    print "Hello World"   #所以当i=5的时候就直接跳出了函数了，这里是不会被打印出来了！不是循环！！！
count()
