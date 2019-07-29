#  フィボナッチ数列を作るプログラム
#  再帰関数とメモ化(?)を使用


def fib(n, plist):
    if n <= 2:
        result = 1
    else:
        result = plist[n - 3] + plist[n - 2]
    return result


def create_fib_list(x):
    fib_list = [0] * x
    for i in range(x):
        fib_list[i] = fib(i + 1, fib_list)
    return fib_list


print("回数(整数):", end="")
count = int(input())
print_list = create_fib_list(count)
print(" ".join(map(str, print_list)))
