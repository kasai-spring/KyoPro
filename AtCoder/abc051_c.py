import sys
# TODO　うまく動作しない(予期せぬ動作)
sx, sy, tx, ty = (int(x) for x in sys.stdin.readline().split())
nowX, nowY = sx, sy
destination_x, destination_y = tx, ty
direction_x, direction_y = 0, 0
history, print_list = [], []
for i in range(4):  # 二往復する
    print(i)
    print(print_list)
    if destination_x - nowX != 0:  # ZeroDivisionError防止
        direction_x = (destination_x - nowX) / abs(destination_x - nowX)
    else:
        direction_x = 0
    if destination_y - nowY != 0:
        direction_y = (destination_y - nowY) / abs(destination_y - nowY)
    else:
        direction_y = 0
    no_move_x = False
    no_move_y = False
    while True:  # x -> y を交互に
        # print(print_list)
        if nowX != destination_x:
            if direction_x >= 0:
                if str(nowX + 1) + str(nowY) in history:
                    if no_move_y:
                        if str(nowX - 1) + str(nowY) in history:
                            no_move_x = True
                        else:
                            nowX -= 1
                            print_list.append("D")
                            history.append(str(nowX) + str(nowY))
                            no_move_x = False
                    else:
                        no_move_x = True
                else:
                    nowX += 1
                    print_list.append("U")
                    history.append(str(nowX) + str(nowY))
                    no_move_x = False
            else:
                if str(nowX - 1) + str(nowY) in history:
                    if no_move_y:
                        if str(nowX + 1) + str(nowY) in history:
                            no_move_x = True
                        else:
                            nowX += 1
                            print_list.append("U")
                            history.append(str(nowX) + str(nowY))
                            no_move_x = False
                    else:
                        no_move_x = True
                else:
                    nowX -= 1
                    print_list.append("D")
                    history.append(str(nowX) + str(nowY))
                    no_move_x = False

        if nowY != destination_y:
            if direction_y >= 0:
                if str(nowX) + str(nowY + 1) in history:
                    if no_move_x:
                        if str(nowX) + str(nowY - 1) in history:
                            no_move_y = True
                        else:
                            nowY -= 1
                            print_list.append("L")
                            history.append(str(nowX) + str(nowY))
                            no_move_y = False
                    else:
                        no_move_y = True
                else:
                    nowY += 1
                    print_list.append("R")
                    history.append(str(nowX) + str(nowY))
                    no_move_y = False
            else:
                if str(nowX) + str(nowY - 1) in history:
                    if no_move_x:
                        if str(nowX) + str(nowY - 1) in history:
                            no_move_y = True
                        else:
                            nowY += 1
                            print_list.append("R")
                            history.append(str(nowX) + str(nowY))
                            no_move_y = False
                    else:
                        no_move_y = True
                else:
                    nowY -= 1
                    print_list.append("L")
                    history.append(str(nowX) + str(nowY))
                    no_move_y = False

        if nowX == destination_x and nowY == destination_y:
            if i % 2 == 0:
                destination_x, destination_y = sx, sy
            else:
                destination_x, destination_y = tx, ty
            break

print("".join(print_list))
