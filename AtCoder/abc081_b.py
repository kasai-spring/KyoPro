import sys

n = int(sys.stdin.readline())
a_list = [int(x) for x in sys.stdin.readline().split()]
count = 0
while True:
    a_list = [i / 2 if i % 2 == 0 else "cant" for i in a_list]
    if "cant" in a_list:
        break
    else:
        count += 1
print(count)
