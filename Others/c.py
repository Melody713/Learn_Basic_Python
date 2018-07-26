#!/usr/bin/env python
# coding=utf-8
count = 0
while True:
    print "我是第一层"
    jump_1_flag = False
    while True:
        print "我是第二层"
        jump_2_flag = False
        while True:
            count += 1
            print "我是第三层"     
            if count > 3:
                jump_2_flag = True
                break
        if jump_2_flag:
            print "第三层跳到我这里来了，我也要跳到第一层"
            jump_1_flag = True
            break
          
    if jump_1_flag:
        print "第二层和第三层跳到第一层了，我也要跳"
        break
