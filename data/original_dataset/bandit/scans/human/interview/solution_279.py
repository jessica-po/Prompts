v1, v2 = list(map(int, input().split()))
t, d = list(map(int, input().split()))
vm = [0] * t

v = v1
for i in range(t):
    vm[i] = v
    v += d

v = v2
for i in range(t - 1, -1, -1):
    vm[i] = min(v, vm[i])
    v += d

print(sum(vm))