# 割り切る数は、Aの総和の約数である
# 自分自身を除く約数について大きい順にすべて試して、当てはまるものがあれば答え

# 8,20を7の倍数に近づけるとき、
# 8 -> mod 7が1であり、-1か+6で7の倍数になる
# 20 -> mod 7が6であり、-6か+1で7の倍数になる
# -1と+1をペアにすることが出来て、この操作回数1をK = 3から引くと2となり、これが偶数ならOK

import sys
readline = sys.stdin.readline

N,K = map(int,readline().split())
A = list(map(int,readline().split()))

all = sum(A)
divisors = []
for i in range(1,int(all ** 0.5) + 1):
  if all % i == 0:
    divisors.append(i)
    divisors.append(all // i)

divisors = sorted(divisors,reverse = True)

#print(divisors)

for d in divisors:
  mods = [0] * (N)
  for i in range(len(A)):
    mods[i] = A[i] % d
  mods = sorted(mods)
  #print("d",d,"mods",mods)
  mods_front = [0] * N
  mods_front[0] = mods[0]
  for i in range(1,N):
    mods_front[i] = mods_front[i - 1] + mods[i]
  mods_back = [0] * N
  mods_back[-1] = d - mods[-1]
  #print("mods_front",mods_front)
  for i in range(N - 2,-1,-1):
    mods_back[i] = mods_back[i + 1] + (d - mods[i])
  #print("mods_back",mods_back)
  for i in range(N - 1):
    if mods_front[i] == mods_back[i + 1]:
      if K >= min(mods_front[i],mods_back[i + 1]):
        print(d)
        return
else:
  print(1)