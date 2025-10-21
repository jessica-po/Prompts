S = input()
T = input()
tigau = 0

for i in range(len(S)):
  if S[i] != T[i]:
    tigau += 1

print(tigau)