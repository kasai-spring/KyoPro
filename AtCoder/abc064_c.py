#  問題文を誤解してたせいでめちゃくちゃ時間がかかった

import sys

n = int(sys.stdin.readline())
a_list = [int(x) for x in sys.stdin.readline().split()]

color_list = [0] * 8
rainbow = 0
for i in a_list:
    if int(i / 400) < 8:
        color_list[int(i / 400)] += 1
    else:
        rainbow += 1
color_list = [i for i in color_list if i != 0]
confirm = len(color_list)
if confirm == 0:
    print(1, min(8, rainbow))
else:
    print(confirm, confirm + rainbow)
