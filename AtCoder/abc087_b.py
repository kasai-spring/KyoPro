A_500 = int(input())
B_100 = int(input())
C_50 = int(input())
X = int(input())
result = 0
for i in range(A_500 + 1):
    for j in range(B_100 + 1):
        for k in range(C_50 + 1):
            if i * 500 + j * 100 + k * 50 == X:
                result += 1
            if i * 500 + j * 100 + k * 50 > X:
                break
print(result)
