a, b = (int(x) for x in input().split())
result = (b ** 2 - a ** 2) / (-2 * a + 2 * b)
if result.is_integer():
    print(int(result))
else:
    print("IMPOSSIBLE")
