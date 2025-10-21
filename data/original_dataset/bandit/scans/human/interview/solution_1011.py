"""
Codeforces Contest 281 Div 2 Problem C

Author  : chaotic_iak
Language: Python 3.3.4
"""

def main():
    n, = read()
    a = read()
    res = [(i,0) for i in a]
    m, = read()
    b = read()
    res.extend((i,1) for i in b)
    res.sort()
    mxa = 3*n
    mnb = 3*m
    cra = 3*n
    crb = 3*m
    for _,i in res:
        if i:
            crb -= 1
            if cra-crb > mxa-mnb:
                mxa = cra
                mnb = crb
        else:
            cra -= 1
    print(str(mxa) + ":" + str(mnb))

################################### NON-SOLUTION STUFF BELOW

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