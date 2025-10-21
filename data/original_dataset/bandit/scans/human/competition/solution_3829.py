"""
Codeforces Contest 259 Div 1 Problem A

Author  : chaotic_iak
Language: Python 3.3.4
"""

def main():
    m,n = read()
    print(m - sum((i/m)**n for i in range(1,m)))

################################### NON-SOLUTION STUFF BELOW

def read(mode=2):
    # 0: String
    # 1: List of strings
    # 2: List of integers
    inputs = input().strip()
    if mode == 0: return inputs
    if mode == 1: return inputs.split()
    if mode == 2: return map(int, inputs.split())

def read_str(): return read(0)
def read_int(): return read(2)[0]

def write(s="\n"):
    if isinstance(s, list): s = " ".join(map(str, s))
    s = str(s)
    print(s, end="")

main()