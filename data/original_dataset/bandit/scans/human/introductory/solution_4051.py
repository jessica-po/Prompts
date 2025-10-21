"""
Codeforces April Fools 2018 Problem C

Author  : chaotic_iak
Language: Python 3.5.2
"""

################################################### SOLUTION

def initialize_solution():
    pass

def main():
    n, = read()
    a = read()
    for i in range(n-1):
        if abs(a[i] - a[i+1]) >= 2:
            return "NO"
    return "YES"

########################################## PROBLEM CONSTANTS

READ_FROM_FILE = None
OUTPUT_PREFIX = None
INTERACTIVE = False

#################################################### HELPERS

import sys

def read(callback=int, split=True):
    if READ_FROM_FILE:
        ipt = sfile.readline().strip()
    else:
        ipt = input().strip()
    if INTERACTIVE and ipt == "WRONG_ANSWER":
        return
    if split:
        return list(map(callback, ipt.split()))
    else:
        return callback(ipt)

def write(value, end="\n"):
    if value is None: return
    try:
        if not isinstance(value, str):
            value = " ".join(map(str, value))
    except:
        pass
    if READ_FROM_FILE:
        tfile.write(str(value, end=end))
    else:
        print(value, end=end)
    if INTERACTIVE:
        sys.stdout.flush()

sfile = None
tfile = None
if READ_FROM_FILE:
    sfile = open(READ_FROM_FILE + ".in", "r")
    sfile.seek(0)
    tfile = open(READ_FROM_FILE + ".out", "w")
if OUTPUT_PREFIX is None:
    result = main()
    if result is not None:
        write(result)
else:
    initialize_solution()
    TOTAL_CASES, = read()
    for CASE_NUMBER in range(1, TOTAL_CASES+1):
        write(OUTPUT_PREFIX.replace("%d", str(CASE_NUMBER)), end="")
        result = main()
        if result is not None:
            write(result)
if sfile is not None: sfile.close()
if tfile is not None: tfile.close()