import os
import nester
import pickle

os.chdir('D:\Python\HeadFirstPython\chapter3')

man = []
other = []
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The file is missing')
try:
    with open('man_speak.txt', 'wb') as man_out, open('other_speak.txt', 'wb') as other_out:
        # nester.print_lol(man, fn=man_out)
        # nester.print_lol(other, fn=other_out)
        pickle.dump(man, man_out)
        pickle.dump(other, other_out)
except IOError as err:
    print('File Error:' + str(err))

except pickle.PickleError as perr:
    print('Pickle Error:' + str(perr))

try:
    with open('man_speak.txt', 'rb') as man_file:
        new_man_file = pickle.load(man_file)
except IOError as err2:
    print('File Error:' + str(err2))
except pickle.PickleError as perr2:
    print('Pickle Error:' +str(perr2))

nester.print_lol(new_man_file)