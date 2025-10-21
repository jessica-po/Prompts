n = int(input())
t = input()
if n == 1:
    if t == "0":
        print((10 ** 10))
    else:
        print((2 * 10 ** 10))
elif n == 2:
    if t == "00":
        print((0))
    elif t == "01":
        print((10 ** 10 - 1))
    elif t == "10":
        print((10 ** 10))
    else:  # 11
        print((10 ** 10))
else:
    repeat_num = (n + 6) // 3
    ref = "110" * repeat_num
    num_in_ref = 0
    flag_over = 0  #
    if ref[:n] == t:
        num_in_ref += 1
        if n % 3 == 0:
            flag_over = 1
    elif ref[1 : n + 1] == t:
        num_in_ref += 1
    elif ref[2 : n + 2] == t:
        num_in_ref += 1
        if n % 3 == 2:
            flag_over = -1
    # print(ref[: n + 1], t)
    print((num_in_ref * (10 ** 10 - repeat_num + 2) + flag_over))