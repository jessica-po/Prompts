from sys import stdin

tt = 1

for loop in range(tt):

    dic = {}
    dic[0] = 1

    n = int(stdin.readline())

    a = list(map(int,stdin.readline().split()))
    now = 0
    ans = 0

    for i in a:
        now += i
        if now in dic:
            ans += 1
            dic = {}
            dic[0] = 1
            now = i
            
        dic[now] = 1

    print (ans)