n,k,m = list(map(int,input().split()))
ai = list(map(int,input().split()))
ai.sort()
n2 = n
num = sum(ai)
ans = 0.0
i = 0
while n2 > 0 and m > -1:
    num2 = (num + min(m,n2 * k)) / n2
    ans = max(ans,num2)
    num -= ai[i]
    i += 1
    n2 -= 1
    m -= 1
print(ans)