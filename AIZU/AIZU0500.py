finish = True
while finish:
    A = 0
    B = 0
    count = int(input())
    if count == 0:
        finish = False
        break
    for i in range(count):
        a, b = (int(x) for x in input().split())
        if a > b:
            A += a + b
        elif a < b:
            B += a + b
        else:
            A += a
            B += b
    print(str(A) + " " + str(B))
