import pickle
import os
from chapter6 import AthleteList

#os.chdir('D:\Python\HeadFirstPython\chapter6')

def get_coach_data(filename):
    try:
        with open(filename) as new_file:
            tmp  = new_file.readline().strip().split(',')
        return AthleteList(tmp.pop(0),tmp.pop(0),tmp)
    except IOError as err:
        print('File Error:' + str(err))
        return None

def put_to_stroe(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath  = get_coach_data(each_file)
        all_athletes[ath.name]  = ath
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes,athf)
    except IOError as ioerr:
        print('File ERROR(put_to_store):' + str(ioerr))
    return all_athletes

def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('File Error(get_from_store):' + str(ioerr))
    return all_athletes

# print(dir())
#
# the_files  = ['sarah2.txt', 'james2.txt', 'julie2.txt', 'mikey2.txt']
# data = put_to_stroe(the_files)
# print(data)
#
# for each_athlete in data:
#     print(data[each_athlete].name + ' ' + data[each_athlete].dob)