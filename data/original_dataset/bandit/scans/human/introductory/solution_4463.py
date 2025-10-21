import sys

input = sys.stdin.readline
s = list(input().strip())
t = list(input().strip())
if sorted(s) < sorted(t, reverse=True):
    print("Yes")
else:
    print("No")