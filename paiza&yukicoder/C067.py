import sys


def bin_k(a, b):
    bin_str = bin(a)
    return list(bin_str)[-b]  # pythonでbin関数を使うと0bが頭につくため


n, x = (int(x) for x in sys.stdin.readline().split())
k = [int(x) for x in sys.stdin.readlines()]
print_list = [bin_k(x, i) for i in k]

for i in print_list:
    print(i)
