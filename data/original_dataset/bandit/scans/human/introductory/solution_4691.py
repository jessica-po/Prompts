c = int(input())

r = ["AC", "WA", "TLE", "RE"]
a = { i:0 for i in r}

for i in range(c):
    s = input()
    a [s] += 1

for rr in r:
    print(rr + " x " + str(a[rr]))