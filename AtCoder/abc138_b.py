n = int(input())
a_list = [int(x) for x in input().split()]
result = 0
for i in a_list:
    result += 1 / i
print(1 / result)
