from collections import defaultdict
n = int(input())
s_dict = defaultdict(int)
for i in range(n):
  s_int = [0] * 26
  s = list(input())
  for si in s:
    s_int[ord(si) - ord('a')] += 1
  cnt = 0
  for s_int_i in s_int:
    cnt *= 10
    cnt += s_int_i
  s_dict[cnt] += 1
ans = 0
for key in s_dict:
  ans += s_dict[key] * (s_dict[key] - 1) / 2
print(int(ans))