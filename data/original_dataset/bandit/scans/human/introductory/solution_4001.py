n = int(input())

seq = sorted(list(map(int, input().split())))[::-1]

a = seq[0]
last = -1
for i in range(len(seq)):
    if a % seq[i] == 0:
        if last != seq[i]:
            last = seq[i]
        else:
            b = seq[i]
            break
    else:
        b = seq[i]
        break
print(a, b)