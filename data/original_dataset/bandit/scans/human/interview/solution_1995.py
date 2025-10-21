s=input()
def shift(x,k):
    x=x[-k:]+x[:-k]
    return x
for i in range(int(input())):
    l,r,k=tuple(map(int,input().split()))
    l-=1
    k%=(r-l)
    s=s[:l]+shift(s[l:r],k)+s[r:]
print(s)