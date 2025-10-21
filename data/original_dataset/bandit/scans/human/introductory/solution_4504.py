S = input()
x = len(S)

for i in range(0, x, 2):
  y = x - 2 - i
  if S[:y//2] == S[y//2 : y]:
    
    print(len(S[:y]))
    break