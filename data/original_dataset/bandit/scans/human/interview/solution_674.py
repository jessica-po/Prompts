n = int(input())

wrong_str = False

strings = []
sets = []
for _ in range(n):
    new_string = input()
    new_string_set = set(new_string)
    if len(new_string) != len(new_string_set):
        wrong_str = True
        break

    strings.append(new_string)
    sets.append(new_string_set)

if wrong_str:
    print("NO")
    return


connections = []
for _ in range(n):
    connections.append((-1,-1))

changed = True

while changed:

    changed = False

    for i in range(len(strings)):

        if strings[i] == None:
            continue

        for j in range(i + 1, len(strings)):

            if strings[j] == None:
                continue

            if len(set(strings[i]).intersection(set(strings[j]))) == 0:
                continue

            a = strings[i]
            b = strings[j]

            #print(a, b)

            if b in a:
                strings[j] = None
                changed = True
            elif a in b:
                strings[i] = b
                strings[j] = None
                changed = True
            else:

                is_ok = False

                start_index = a.find(b[0])
                if start_index != -1 and a[start_index:] in b:
                    strings[i] += strings[j][len(a) - start_index:]
                    strings[j] = None
                    is_ok = True
                    changed = True

                if not is_ok:
                    start_index = b.find(a[0])
                    if start_index != -1 and  b[start_index:] in a:
                        strings[i] = strings[j] + strings[i][len(b) - start_index:]
                        strings[j] = None
                        is_ok = True
                        changed = True

                if not is_ok:
                    print("NO")
                    return




        if wrong_str:
            print("NO")
            return

    strings = [x for x in strings if x is not None]

whole_str = "".join(strings)

if len(whole_str) != len(set(whole_str)):
    print("NO")
    return

print("".join(sorted(strings)))