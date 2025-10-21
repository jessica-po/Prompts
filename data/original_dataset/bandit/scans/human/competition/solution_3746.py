#	!/bin/env python3
#	coding: UTF-8


#	✪ H4WK3yE乡
#	Mohd. Farhan Tahir
#	Indian Institute Of Information Technology and Management,Gwalior

#	Question Link
#	https://codeforces.com/problemset/problem/392/B
#

# ///==========Libraries, Constants and Functions=============///


import sys

inf = float("inf")
mod = 1000000007


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return list(map(int, sys.stdin.readline().split()))


def input(): return sys.stdin.readline()

# ///==========MAIN=============///


def main():
    dp = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(43)]
    matrix = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        matrix[i] = get_array()
    n = int(input())
    for i in range(1, n+1):
        for frm in range(3):
            for to in range(3):
                other = 3-frm-to
                if frm == to:
                    continue
                dp[i][frm][to] = dp[i-1][frm][other]+matrix[frm][to]+dp[i-1][other][to]
                c = dp[i-1][frm][to]+matrix[frm][other] + \
                    dp[i-1][to][frm]+matrix[other][to]+dp[i-1][frm][to]
                dp[i][frm][to] = min(c, dp[i][frm][to])
    print(dp[n][0][2])


def __starting_point():
    main()

__starting_point()