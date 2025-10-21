input()
memory = list(map(int, input().split()))

proc_data = {p: (-1, -1) for p in memory}

for i, c in enumerate(memory):
    d1, d2 = proc_data[c]
    if d1 == -1: d1 = i
    d2 = i
    proc_data[c] = (d1, d2)

try: del proc_data[0]
except KeyError:
    print("0")
    return

data = list(proc_data.values())
data.sort()

ans = 0

first_free = 0

for a, b in data:
    c = a - first_free
    ans += min(c, b-a+1)
    b -= c
    first_free = b + 1

print(ans)