"""
Codeforces Good Bye 2016 Contest Problem C

Author  : chaotic_iak
Language: Python 3.5.2
"""

################################################### SOLUTION

def main():
    n, = read()
    mn, mx = -10**18, 10**18
    for _ in range(n):
        c, d = read()
        if d == 1:
            mn = max(mn, 1900)
        elif d == 2:
            mx = min(mx, 1899)
        mn += c
        mx += c
    if mn > mx:
        print("Impossible")
        return
    if mx > 10**17:
        print("Infinity")
        return
    print(mx)

#################################################### HELPERS

def read(callback=int):
    return list(map(callback, input().strip().split()))

def write(value, end="\n"):
    if value is None: return
    try:
        value = " ".join(map(str, value))
    except:
        pass
    print(value, end=end)

write(main())