#!/usr/bin/env python
# coding=utf-8

with open('/root/start.sh','r') as job1,open('aaa','w') as job2:
    for i in job1.readlines():
        i = i.strip()
        print i
        job2.write(i)
        job2.write('\n')
