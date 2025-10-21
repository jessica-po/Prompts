import sys

n, k = map(int, input().split())
a = list(map(int, input().split()))

cur_max = 0
last_max = 1
last = dict()
zeros = []

for i in range(len(a))[::-1]:
    if a[i] == 0:
        zeros.append(i)
    elif a[i] not in last:
        last[a[i]] = i

stack = []

for i in range(len(a)):
    if a[i] == 0:
        a[i] = max(cur_max, 1)
    elif a[i] > cur_max and last[a[i]] != i:
        stack.append(cur_max)
        cur_max = a[i]
    elif cur_max != 0 and i == last[cur_max]:
        cur_max = stack.pop()
    elif a[i] < cur_max:
        print("NO")
        return

if k > max(a):
    if zeros:
        print("YES")
        a[zeros[0]] = k
        print(*a)
    else:
        print("NO")
elif k == max(a):
    print("YES")
    print(*a)
elif k < max(a):
    print("NO")