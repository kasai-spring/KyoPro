n, a, b = (int(x) for x in input().split())
result = 0
for i in range(1, n + 1):
    if a <= sum([int(x) for x in str(i)]) <= b:
        result += i
print(result)
