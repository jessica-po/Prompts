def main():
    n, k = list(map(int, input().split()))
    even = 0
    odd = 0
    for elem in input().split():
        if int(elem) % 2 == 0:
            even += 1
        else:
            odd += 1
    turns = n - k
    if turns == 0:
        if odd % 2 == 1:
            return "Stannis"
        else:
            return "Daenerys"
    if turns % 2 == 0:
        if k % 2 == 1 and even <= turns // 2:
            return "Stannis"
        else:
            return "Daenerys"
    else:
        if k % 2 == 0 and even <= turns // 2 or odd <= turns // 2:
            return "Daenerys"
        else:
            return "Stannis"
print(main())