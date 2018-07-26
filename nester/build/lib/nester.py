#musics = ["gold you come","olwcity","2010","albert",["kobe",["lakers","sg","mvp"]]]
import sys

# def print_lol(the_list):
#     for each_one in the_list:
#         if isinstance(each_one, list):
#             print_lol(each_one)
#         else:
#             print(each_one)

def print_lol(the_list, indent=False, level=0, fn=sys.stdout):
    for each_one in the_list:
        if isinstance(each_one, list):
            print_lol(each_one, indent, level+1, fn)
        else:
            if indent:
                for level_num in range(level):
                    print("\t", end='', file=fn)
            print(each_one, file=fn)

# print_lol(musics,False,0)
