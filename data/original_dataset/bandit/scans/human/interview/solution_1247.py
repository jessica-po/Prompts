def __starting_point():
    s = input()
    c = [s.count(x) for x in set(s)]
    total = 0
    for x in c:
        if x % 2 != 0:
            total += 1
    if total % 2 == 0 and total != 0:
        print("Second")
    else:
        print("First")

__starting_point()