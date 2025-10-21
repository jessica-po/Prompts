#写経
#https://atcoder.jp/contests/abc168/submissions/13414936
from math import gcd
from collections import Counter
mod = 10**9 + 7
N,*AB = map(int,open(0).read().split())

def std(a,b):
    """
    a,bを既約にする
    """
    if a == 0:
        return(0,int(b!=0))
    g = gcd(a,b)
    a,b = a// g, b//g
    return(a,b) if a > 0 else (-a,-b)

C = Counter(std(a, b) for a, b in zip(*[iter(AB)] * 2))
def resolve():
    ans = 1
    cnt = 0
    for (a,b), v in C.items():
        if b > 0:
            if (b,-a) in C:
                ans *= -1 + pow(2,v,mod) + pow(2,C[(b,-a)], mod) #仲の悪い組み合わせが一緒に入らないように，別々に入れるか入れないかを判定 空集合は共通しているので引く
                ans %= mod
            else:
                cnt += v
        elif (-b,a) not in C:
            cnt += v
    ans *= pow(2,cnt,mod)
    ans += C[(0,0)] - 1
    print(ans%mod)
resolve()