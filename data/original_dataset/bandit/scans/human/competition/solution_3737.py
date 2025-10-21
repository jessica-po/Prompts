x = int(input())
l = list(map(int, input().split(' ')))
if min(l) == max(l):
    print(0)
else:
    print(x-l.count(min(l))-l.count(max(l)))