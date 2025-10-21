"""
Codeforces Rockethon Contest Problem A

Author  : chaotic_iak
Language: Python 3.4.2
"""

################################################### SOLUTION

def main():
    n1,n2,k1,k2 = read()
    if n1 > n2:
        return "First"
    return "Second"



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