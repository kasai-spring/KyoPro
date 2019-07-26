import sys

n = int(sys.stdin.readline())
txy = [[int(x) for x in sys.stdin.readline().split()] for y in range(n)]
nowX, nowY = 0, 0
t = 0
for i in range(len(txy)):
    time_limit = txy[i][0] - t
    distance_x = abs(txy[i][1] - nowX)
    distance_y = abs(txy[i][2] - nowY)
    distance = distance_x + distance_y
    if time_limit < distance:  # そもそも最短距離を通っても到着地点にたどり着けない場合
        print("No")
        break
    if time_limit % 2 == distance % 2:
        t, nowX, nowY = txy[i][0], txy[i][1], txy[i][2]
    else:
        print("No")
        break
else:
    print("Yes")
