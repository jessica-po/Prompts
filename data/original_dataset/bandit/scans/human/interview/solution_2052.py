w, l = [int(i) for i in input().split(' ')]
arr = [int(i) for i in input().split(' ')]

cummulative = [0 for i in range(len(arr) + 1)]
for i in range(len(arr)):
    cummulative[i+1] = cummulative[i] + arr[i]

min_cut = 1000000009

for i in range(w - l):
    cut = cummulative[i + l] - cummulative[i]
    if cut < min_cut:
        min_cut = cut

print(min_cut)