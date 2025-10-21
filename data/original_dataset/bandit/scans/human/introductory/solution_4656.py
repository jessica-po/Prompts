t = int(input())
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
for _ in range(t):
    n,k = map(int,input().split())
    s = input()
    occ = [0] * 26
    for i in s:
        occ[ord(i)-97] += 1
    occ.sort()
    occ.reverse()
    for l in range(1,n+1):
        cycle = gcd(l,k)
        need = l//cycle
        su = 0
        for i in occ:
            su += i//need
        if su*need >= l:
            wyn = l
    print(wyn)