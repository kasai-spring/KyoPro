while True:
    name, _type = input().split()
    if _type == "X":
        break
    name_list = list(name)
    if _type == "U":
        name_list[0] = name_list[0].upper()
        if "_" in name_list:
            for i in range(len(name_list)):
                try:
                    if name_list[i] == "_":
                        name_list[i + 1] = name_list[i + 1].upper()
                        del name_list[i]
                except IndexError:
                    break

    elif _type == "L":
        name_list[0] = name_list[0].lower()
        if "_" in name_list:
            for i in range(len(name_list)):
                try:
                    if name_list[i] == "_":
                        name_list[i + 1] = name_list[i + 1].upper()
                        del name_list[i]
                except IndexError:
                    break

    elif _type == "D":
        under_counter = 0
        under_insert_loc = []
        name_list[0] = name_list[0].lower()
        for i in range(len(name_list)):
            if name_list[i].isupper():
                name_list[i] = name_list[i].lower()
                under_insert_loc.append(i + under_counter)
                under_counter += 1
        for i in under_insert_loc:
            name_list.insert(i, "_")

    print("".join(name_list))
