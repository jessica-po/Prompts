k = int(input().split()[1])
a = [int(s) for s in input().split()]
b = [int(s) for s in input().split()]
ambk = [(a[i], a[i] - b[i]*k) for i in range(len(a))]
ambk.sort(key=lambda a:-a[1])

ts = [0]*(100*100)
keys = [0]
atras = list(range(100*100 -1, -1, -1))
adelante = list(range(100*100))
for i in range(len(a)):
  for j in ( atras if ambk[i][1] >= 0 else adelante ):
    if ts[j] > 0 or j == 0:
      if j + ambk[i][1] >= 0:
        ts[j+ambk[i][1]] = max(ts[j+ambk[i][1]], ts[j] + ambk[i][0])

print("-1" if ts[0] == 0 else str(ts[0]))