"""
Codeforces Contest 260 Div 1 Problem A

Author  : chaotic_iak
Language: Python 3.3.4
"""

def main():
    n, = read()
    ar = read()
    a = [0] * 100001
    for i in ar: a[i] += 1

    dp = [0] * 100001
    dp[1] = a[1]
    for i in range(2, 100001):
        dp[i] = max(a[i] * i + dp[i-2], dp[i-1])
    print(dp[-1])

################################### NON-SOLUTION STUFF BELOW

def read(mode=2):
    # 0: String
    # 1: List of strings
    # 2: List of integers
    inputs = input().strip()
    if mode == 0: return inputs
    if mode == 1: return inputs.split()
    if mode == 2: return map(int, inputs.split())

def write(s="\n"):
    if isinstance(s, list): s = " ".join(map(str, s))
    s = str(s)
    print(s, end="")

main()