def coloring(i, ancestors, color):
    while i != 0 and color[ancestors[i - 1]] is None:
        color[ancestors[i - 1]] = not color[i]
        i = ancestors[i - 1]


def main():
    n = int(input())
    a = list(map(int, input().split()))
    ancestors = list([int(x) - 1 for x in input().split()])
    descendants = [[] for i in range(n)]
    for i in range(n - 1):
        descendants[ancestors[i]].append(i + 1)
    color = [None for i in range(n)]
    for i in range(n):
        if not descendants[i]:
            color[i] = True
            coloring(i, ancestors, color)
    reds = 0
    blues = 0
    xor = 0
    count_red = dict()
    count_blue = dict()
    for i in range(n):
        if color[i]:
            blues += 1
            xor ^= a[i]
            if str(a[i]) in count_blue:
                count_blue[str(a[i])] += 1
            else:
                count_blue[str(a[i])] = 1
        else:
            reds += 1
            if str(a[i]) in count_red:
                count_red[str(a[i])] += 1
            else:
                count_red[str(a[i])] = 1
    res = 0
    if xor == 0:
        res += (blues - 1) * blues // 2
        res += (reds - 1) * reds // 2
        for i in list(count_blue.items()):
            if i[0] in count_red:
                res += i[1] * count_red[i[0]]
    else:
        for i in list(count_blue.items()):
            if str(xor ^ int(i[0])) in count_red:
                res += i[1] * count_red[str(xor ^ int(i[0]))]
    print(res)


main()