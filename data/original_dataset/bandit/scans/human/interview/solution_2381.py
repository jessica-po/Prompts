n, k = [int(x) for x in input().strip().split(" ")]
p = 10**9 + 7

num_list = [int(x) for x in input().strip().split(" ")]
num_list = sorted(num_list, reverse = True)

ans = 1
l_idx = 0
r_idx = -1

if num_list[0] < 0 and k % 2 == 1:
  for i in range(k):
    ans = (ans * num_list[i]) % p
else:
  while True:
    if k >= 2:
      l_prod = num_list[l_idx] * num_list[l_idx+1]
      r_prod = num_list[r_idx] * num_list[r_idx-1]
      if l_prod >= r_prod:
        ans = (ans * num_list[l_idx]) % p
        l_idx +=1
        k -= 1
      else:
        ans = (ans * r_prod) % p
        r_idx -=2
        k -= 2
    elif k == 1:
      ans = (ans * num_list[l_idx]) % p
      ans %= p
      break
    else:
      break

print(ans)