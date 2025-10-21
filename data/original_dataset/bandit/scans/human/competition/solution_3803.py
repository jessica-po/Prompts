H_y,A_y,D_y = list(map(int,input().split()))
H_m,A_m,D_m = list(map(int,input().split()))
h,a,d = list(map(int,input().split()))
ans = 10**20
for A_buy in range(max(0,H_m+D_m-A_y)+1):
  for D_buy in range(max(0,A_m-D_y)+1):
    damage = A_y + A_buy - D_m
    cost = A_buy * a + D_buy * d
    if damage > 0 and cost < ans:
      time = (H_m+damage-1)//damage
      H_left = H_y - time * max(0, A_m - D_y - D_buy)
      if H_left <= 0: cost += h * (1-H_left)
      if cost < ans: 
        ans = cost
print(ans)