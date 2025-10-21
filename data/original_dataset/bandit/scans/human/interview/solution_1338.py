"""
Codeforces Rockethon Contest Problem B

Author  : chaotic_iak
Language: Python 3.4.2
"""

################################################### SOLUTION

def main():
    n,m = read()
    m -= 1
    perm = [0]*n
    lf = 0
    rt = n-1
    for i in range(n):
        if m >= 2**(n-i-2):
            perm[rt] = i+1
            rt -= 1
        else:
            perm[lf] = i+1
            lf += 1
        m %= 2**(n-i-2)
    write(perm)



#################################################### HELPERS



def read(mode=2):
    # 0: String
    # 1: List of strings
    # 2: List of integers
    inputs = input().strip()
    if mode == 0: return inputs
    if mode == 1: return inputs.split()
    if mode == 2: return list(map(int, inputs.split()))

def write(s="\n"):
    if s is None: s = ""
    if isinstance(s, list): s = " ".join(map(str, s))
    s = str(s)
    print(s, end="")

write(main())