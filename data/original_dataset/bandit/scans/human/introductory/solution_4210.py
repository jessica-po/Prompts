inp = input().split()
n = int(inp[0])
k = int(inp[1])

a = input().split()
for i in range(n):
    a[i] = int(a[i])

# End of Input

bank  = {}

# Preparation
for i in range(n):
    arg = (len(str(a[i])),a[i]%k)
    #print("Detect:",arg)
    bank[arg] = bank.get(arg,0)+1

ans = 0
# Query
for i in range(n):
    ten = 1
    for j in range(1,11):
        ten*=10
        frontMod = (a[i]*ten)%k
        #print("FRONT MOD:",frontMod)
        req = (k-frontMod)%k
        #print("WANT:",req)

        got = bank.get((j,req),0)
        ans += got

# Deal with Same Index
for i in range(n):
    cur = str(a[i])
    cur = cur*2
    tst = int(cur)
    if(tst%k==0):
        ans-=1

# Print Answer
print(ans)