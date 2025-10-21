import sys
input = sys.stdin.readline

m, n = list(map(int, input().split()))
Dora = []
Swiper = []
all = set([i for i in range(1, n+1)])
for _ in range(m):
    a = set(list(map(int, input().split()))[1:])
    Dora.append(a)
    Swiper.append(all.difference(a))

flag = 1
for i in range(m):
    for j in range(m):
        if Dora[i] | Swiper[j] == Swiper[j]:
            flag = 0
            break
    if flag == 0:
        break

if flag == 1:
    print("possible")
else:
    print("impossible")