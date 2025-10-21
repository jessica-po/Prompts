import sys

fin = sys.stdin
fout = sys.stdout

#fin = open("input.txt", 'r')
#fout = open("output.txt", 'w')

s = fin.readline().strip()
n = len(s)
for L in range(n):
    for R in range(L + 1, n + 1):
        s1 = s[:L]
        s2 = s[L:R]
        s3 = s[R:]
        if (s1 + s3 == "CODEFORCES"):
            print("YES")
            return
print("NO")