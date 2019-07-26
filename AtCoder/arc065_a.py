#  今思えばreplaceでeraser - erase - dreamer dream の順で置換していったほうが圧倒的にコードが見やすくなったと思う...
s_list = list(input())
while True:
    # 4種類の単語を特定し都度削除していく
    if len(s_list) == 0:
        print("YES")
        break
    try:
        # dreamer or dream
        if s_list[:5] == ["d", "r", "e", "a", "m"]:
            try:
                # この場合だけdreamer
                if s_list[5:7] == ["e", "r"]:
                    try:
                        if s_list[7] == "a":
                            del s_list[:5]
                        else:
                            del s_list[:7]
                    except IndexError:
                        del s_list[:7]
                else:
                    del s_list[:5]
            except IndexError:
                del s_list[:5]
        # eraser or erase
        elif s_list[:5] == ["e", "r", "a", "s", "e"]:
            try:
                if s_list[5] == "r":
                    del s_list[:6]
                else:
                    del s_list[:5]
            except IndexError:
                del s_list[:5]
        else:
            print("NO")
            break
    except IndexError:
        print("NO")
        break
