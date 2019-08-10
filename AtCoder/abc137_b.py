k, x = (int(x) for x in input().split())
ans = [x for x in range(max(-1000000, x - k + 1), min(1000000, x + k))]
print(" ".join(map(str, ans)))
