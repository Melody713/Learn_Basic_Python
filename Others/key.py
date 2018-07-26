#!/usr/bin/env python
# coding=utf-8

a=[11,12,13,14,16,17,18,19,20]
dict1={}


for i in a:
    if i > 15:
        if 'key1' in dict1.keys():
            dict1['key1'].append(i)
        else:
            dict1['key1']=[i,]
    else:
        if 'key2' in dict1.keys():
            dict1['key2'].append(i)
        else:
            dict1['key2']=[i,]

print dict1
