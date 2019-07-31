import time
import copy
listA = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2],
        [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2]]
count = 100000
time_start = time.time()
for i in range(count):
    test = [[x for x in y] for y in listA]
time_for = time.time() - time_start
time_start = time.time()
for i in range(count):
    test = copy.deepcopy(listA)
time_deepcopy = time.time() - time_start
print("for文", time_for, "秒")
print("deepcopy", time_deepcopy, "秒")
