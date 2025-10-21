def check(s,k):
    for i in range(k+1):
        if chr(ord('0')+i) not in s: 
            return False
    return True


n, k = map(int,input().split())
ans = 0
for i in range(n):
    ss = input()
    if check(ss,k):
        ans +=1
print(ans)