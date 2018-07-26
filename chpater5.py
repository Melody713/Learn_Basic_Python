import os
import nester

os.chdir('D:\Python\HeadFirstPython\chapter5')

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

def clean_data(file):
    try:
        with open(file) as new_file:
            data = new_file.readline()
        return(data.strip().split(','))
    except IOError as err:
        print('File Error:' + str(err))
        return (None)

james = clean_data('james.txt')
julie = clean_data('julie.txt')
mikey = clean_data('mikey.txt')
sarah = clean_data('sarah.txt')

print(sorted(set([sanitize(each_t) for each_t in james]))[0:3])
print(sorted(set([sanitize(each_t) for each_t in julie]))[0:3])
print(sorted(set([sanitize(each_t) for each_t in mikey]))[0:3])
print(sorted(set([sanitize(each_t) for each_t in sarah]))[0:3])
# clean_julie = sorted([sanitize(each_t) for each_t in julie])
# clean_mikey = sorted([sanitize(each_t) for each_t in mikey])
# clean_sarah = sorted([sanitize(each_t) for each_t in sarah])
# try:
#     with open('james.txt') as jf, open('julie.txt') as juf, open('mikey.txt')as mf, open('sarah.txt')as sf:
#         data = jf.readline()
#         james = data.strip().split(',')
#         data = juf.readline()
#         julie = data.strip().split(',')
#         data = mf.readline()
#         mikey = data.strip().split(',')
#         data = sf.readline()
#         sarah = data.strip().split(',')

        # clean_james = []
        # clean_julie = []
        # clean_mikey = []
        # clean_sarah = []
        #
        # for each_t in james:
        #     clean_james.append(sanitize(each_t))
        # for each_t in julie:
        #     clean_julie.append(sanitize(each_t))
        # for each_t in mikey:
        #     clean_mikey.append(sanitize(each_t))
        # for each_t in sarah:
        #     clean_sarah.append(sanitize(each_t))

        # clean_james = sorted([sanitize(each_t) for each_t in james])
        # clean_julie = sorted([sanitize(each_t) for each_t in julie])
        # clean_mikey = sorted([sanitize(each_t) for each_t in mikey])
        # clean_sarah = sorted([sanitize(each_t) for each_t in sarah])

        # james = sorted([sanitize(each_t) for each_t in james])
        # julie = sorted([sanitize(each_t) for each_t in julie])
        # mikey = sorted([sanitize(each_t) for each_t in mikey])
        # sarah = sorted([sanitize(each_t) for each_t in sarah])

        # james = sorted(set([sanitize(each_t) for each_t in james]))[0:3]
        # julie = sorted(set([sanitize(each_t) for each_t in julie]))[0:3]
        # mikey = sorted(set([sanitize(each_t) for each_t in mikey]))[0:3]
        # sarah = sorted(set([sanitize(each_t) for each_t in sarah]))[0:3]
        #
        # print(james)
        # print(julie)
        # print(mikey)
        # print(sarah)

        # unique_james = []
        # for t in james:
        #     if t not in unique_james:
        #         unique_james.append(t)
        # print(unique_james)

        # print(clean_james)
        # print(clean_julie)
        # print(clean_mikey)
        # print(clean_sarah)

# except IOError as err:
#     print("File Error:" + str(err))



