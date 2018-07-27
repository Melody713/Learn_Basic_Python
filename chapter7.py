import pickle
import os
from chapter6 import AthleteList

os.chdir('D:\Python\HeadFirstPython\chapter6')

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

    return all_athletes

def get_from_store():
    all_athletes = {}

    return all_athletes