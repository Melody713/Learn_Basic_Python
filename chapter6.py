import os
os.chdir('D:\Python\HeadFirstPython\chapter6')

# class NamedList(list):
#     def __init__(self, a_name):
#         list.__init__([])
#         self.name = a_name

# class Athlete:
#     def __init__(self, a_name, a_dob=None, a_times=[]):
#         self.name = a_name
#         self.dob = a_dob
#         self.times = a_times
#
#     def top3(self):
#         return sorted(set([sanitize(t) for t in self.times]))[0:3]
#
#     def add_time(self, time_value):
#         self.times.append(time_value)
#
#     def add_times(self, list_of_values):
#         self.times.extend(list_of_values)
class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
    def top3(self):
        return sorted(set([sanitize(t) for t in self]))[0:3]

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs

def get_coach_data(filename):
    try:
        with open(filename) as new_file:
            #data = new_file.readline()
            tmp  = new_file.readline().strip().split(',')
        return AthleteList(tmp.pop(0),tmp.pop(0),tmp)
        # return data.strip().split(',')
        # return {'Name':tmp.pop(0),
        #         'DOB':tmp.pop(0),
        #         'Times': str(sorted(set([sanitize(t) for t in tmp]))[0:3])}
    except IOError as err:
        print('File Error:' + str(err))
        return None
james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')
print(james.name + "'s fastest times are:" + str(james.top3()))
print(julie.name + "'s fastest times are:" + str(julie.top3()))
print(mikey.name + "'s fastest times are:" + str(mikey.top3()))
print(sarah.name + "'s fastest times are:" + str(sarah.top3()))

# vera = AthleteList('vera vi')
# vera.append('1.31')
# print(vera.top3())
# vera.extend(['2.22','1-21','2:22'])
# print(vera.top3())


# def get_coach_data(filename):
#     try:
#         with open(filename) as new_file:
#             data = new_file.readline()
#         return data.strip().split(',')
#     except IOError as err:
#         print('File Error:' + str(err))
#         return None

# print(james['Name']+ "'s fastest times are:" + james['Times'])
# sarah = get_coach_data('sarah2.txt')

# (sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
# print(sarah_name + "'s fastest times are: " +
#       str(sorted(set([sanitize(t) for t in sarah]))[0:3]))


# sarah_data  = dict()
# sarah_data['Name'] = sarah.pop(0)
# sarah_data['Birthday'] = sarah.pop(0)
# sarah_data['Times'] = sarah
#
# print(sarah_data['Name'] + "'s fastest times are:" + str(sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]))
