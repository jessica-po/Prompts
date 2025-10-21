N = int(input())

# N!を(10^9+7)で割った余りを求める
# N!そのものを求める必要はなく、
# x = i*x (mod 10^9+7) と更新していけばよい
M = 10**9 + 7
s = 1
for i in range(1, N+1):
  s *= i
  s %= M
  
print(s)