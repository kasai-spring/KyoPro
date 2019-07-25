import copy
strin = list(input())
q = int(input())
for i in range(q):
    inputA = input().split()
    if inputA[0] == "replace":
        start = int(inputA[1])
        end = int(inputA[2])+1
        replacer = list(inputA[3])
        count = 0
        for j in range(start,end):
            strin[j] = replacer[count]
            count += 1

    elif inputA[0] == "reverse":
        start = int(inputA[1])
        end = int(inputA[2])+1
        reverser = copy.copy(strin)
        reverser = reverser[start:end]
        reverser = reverser[::-1]
        count = 0
        for j in range(start,end):
            strin[j] = reverser[count]
            count += 1

    else:
        start = int(inputA[1])
        end = int(inputA[2])+1
        for j in range(start,end):
            print(strin[j], end="")
        else:
            print()

