n = int(input())
a = [int(i) for i in input().split()]
a.sort()
a.reverse()
for i in a:
    if i < 0:
        print(i)
        return
    if int(i ** 0.5) ** 2 != i:
        print(i)
        return