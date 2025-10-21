_n = input()
lines = list(map(int, input().split()))
lines.sort()
longest = lines.pop()
if sum(lines) > longest:
  print("Yes")
else:
  print("No")