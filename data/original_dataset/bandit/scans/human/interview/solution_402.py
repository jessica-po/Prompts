"""
Codeforces Good Bye 2016 Contest Problem A

Author  : chaotic_iak
Language: Python 3.5.2
"""

################################################### SOLUTION

def main():
    n,k = read()
    avail = 240-k
    i = 1
    while i <= n and avail >= 5*i:
        avail -= 5*i
        i += 1
    print(i-1)

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