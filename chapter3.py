import os

os.chdir('D:\Python\HeadFirstPython\chapter3')

try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            if not each_line.find(':')== -1:
                (role, line_spoken) = each_line.split(':',1)
                print(role, end='')
                print(' said:', end='')
                print(line_spoken, end='')
        except:
            pass
    data.close()
except IOError:
    print('This file is messing!')