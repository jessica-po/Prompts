"""
Codeforces Good Bye 2016 Contest Problem B

Author  : chaotic_iak
Language: Python 3.5.2
"""

################################################### SOLUTION

def main():
    latitude = 0
    n, = read()
    for i in range(n):
        l, d = read(str)
        l = int(l)
        if latitude == 0:
            if d != "South":
                return "NO"
        if latitude == 20000:
            if d != "North":
                return "NO"
        if d == "South":
            latitude += l
        elif d == "North":
            latitude -= l
        if not (0 <= latitude <= 20000):
            return "NO"
    if latitude != 0:
        return "NO"
    return "YES"

#################################################### HELPERS

def read(callback=int):
    return list(map(callback, input().strip().split()))

def write(value, end="\n"):
    if value is None: return
    try:
        if not isinstance(value, str):
            value = " ".join(map(str, value))
    except:
        pass
    print(value, end=end)

write(main())