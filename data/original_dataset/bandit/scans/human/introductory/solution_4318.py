N = int(input())
H = list(map(int,input().split()))

top = H[0]
cnt = 1

for i in range(1,N):
  if top <= H[i]:
    cnt += 1
    top = H[i]

print(cnt)