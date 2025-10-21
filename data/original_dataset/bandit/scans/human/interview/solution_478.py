from sys import stdin
input = stdin.readline

n = int(input())
s = list(input().strip())

for i in range(26):
    char = chr(ord('z') - i)
    prev = chr(ord('z') - i - 1)

    updated = True
    while updated:
        updated = False
        for idx in range(len(s)-1, -1, -1):
            if s[idx] == char:
                if idx < len(s)-1 and s[idx+1] == prev:
                    s.pop(idx)
                    updated = True
                elif idx > 0 and s[idx-1] == prev:
                    s.pop(idx)
                    updated = True

print( n - len(s))