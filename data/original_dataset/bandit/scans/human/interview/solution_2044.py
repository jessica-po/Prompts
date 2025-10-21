import sys
import io

stream_enable = 0

inpstream = """
3 5
3 7 9

"""

if stream_enable:
    sys.stdin = io.StringIO(inpstream)
    input()

def inpmap():
    return list(map(int, input().split()))

n, m = inpmap()
arr = inpmap()
s = 0
for x in arr:
    s += x
    print(s // m, end=' ')
    s %= m
print()