n=int(input())
a=[int(x) for x in input().rstrip().split()]

now=1
mod=10**9+7
def lcm(a,b):#最小公倍数
    ori_a=a
    ori_b=b
    while b!=0:
        a,b=b,a%b
    return (ori_a*ori_b)//a
  
for i in a:
  now=lcm(i,now)
# print(now)
print((sum([now//i for i in a])%mod))