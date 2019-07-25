import sys

n, m = (int(x) for x in sys.stdin.readline().split())
city_list = [[int(x) for x in sys.stdin.readline().split()] for y in range(m)]
print_list = [0] * m
count = 0
pref_dic = {}
for i in range(len(city_list)):
    city_list[i].append(i)
city_list.sort(key=lambda x: (x[0], x[1]))
for i in city_list:
    pref = i[0]
    pref_id = "0" * (6 - len(str(pref))) + str(pref)
    city_id = ""
    if pref in pref_dic:
        pref_dic[pref] += 1
        city = pref_dic[pref]
        city_id = "0" * (6 - len(str(city))) + str(city)
    else:
        pref_dic[pref] = 1
        city_id = "0" * (6 - len(str(1))) + str(1)
    print_list[i[2]] = pref_id + city_id

for i in print_list:
    print(i)
