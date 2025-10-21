from sys import stdin, stdout, exit

mod = 998244353

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

ans = 0

def l(x):
    if x == 0:
        return 0
    return 1 + l(x//10)

lens = [0]*15
for x in a:
    lens[l(x)] += 1

def space_out(x, l):
    ans = []
    for i,c in enumerate(reversed(str(x))):
        ans.append(c)
        if i < l:
            ans.append("0")
    return int(''.join(reversed(ans))) 

for i in range(n):
    x = a[i]
    cur_head = x//10
    cur = x
    prev = x
    for l in range(11):
#        print(cur, cur_head)
        if l > 0:
            ans += lens[l]*(cur+10*prev)#space_out(x,l)
            ans %= mod
        prev = cur
        cur -= cur_head*10**(2*l+1)
        cur += cur_head*10**(2*l+2)
        cur_head //=10


stdout.write(str(ans) + "\n")