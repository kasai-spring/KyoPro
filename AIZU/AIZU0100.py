finish = 0
while finish < 1:
    N = int(input())
    if N == 0:
        finish += 1
        break
    employee = {}
    for i in range(N):
        e, p, q = (int(x) for x in input().split())
        if e in employee:
            employee[e] += p * q
        else:
            employee[e] = p * q
    count = 0
    for i in employee:
        if employee[i] >= 1000000:
            count += 1
            print(i)
    if count == 0:
        print("NA")
