import sys
s = input().strip()

def isPalin(n):
    if n[::-1] == n:
        return True
    return False

for i in range(len(s)+1):
    for j in "abcdefghijklmnopqrstuvwxyz":
        if isPalin(s[:i] + j + s[i:]):
            print(s[:i] + j + s[i:])
            return

print("NA")