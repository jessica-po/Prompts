n, k = map(int, input().split())
v = list(map(int, input().split()))
reverse_v = v[::-1]
lst = [0] * (k + 1)
left = [[]]
right = [[]]
for i in range(1, n+1):
  left.append(v[:i])
  right.append(reverse_v[:i])

for cnt in range(1, k+1):
  rest = k - cnt
  total = 0
  if cnt <= n:
    for j in range(cnt+1):
      lst_j = left[j] + right[cnt-j]
      lst_j.sort()
      l = cnt
      for idx in range(cnt):
        if lst_j[idx] >= 0:
          l = idx
          break
      if l == cnt:
        value = 0
      else:
        flg = min(l, rest)
        value = sum(lst_j[flg:])
      if value > total:
        total = value
    lst[cnt] = total

ans = max(lst)
print(ans)