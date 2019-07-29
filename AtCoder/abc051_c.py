sx, sy, tx, ty = (int(x) for x in input().split())
print_list = []
# 一回目
for i in range(abs(tx - sx)):
    print_list.append("R")
for i in range(abs(ty - sy)):
    print_list.append("U")
# 二回目
for i in range(abs(tx - sx)):
    print_list.append("L")
for i in range(abs(ty - sy)):
    print_list.append("D")
# 三回目
print_list.append("D")
for i in range(abs(tx - sx) + 1):
    print_list.append("R")
for i in range(abs(ty - sy) + 1):
    print_list.append("U")
print_list.append("L")
# 四回目
print_list.append("U")
for i in range(abs(tx - sx) + 1):
    print_list.append("L")
for i in range(abs(ty - sy) + 1):
    print_list.append("D")
print_list.append("R")
print("".join(print_list))
