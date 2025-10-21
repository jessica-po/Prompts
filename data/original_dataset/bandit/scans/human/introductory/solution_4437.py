import sys
input = sys.stdin.readline

n=int(input())
s=list(input().strip())

ANS=0
for i in range(0,n,2):
    if s[i]==s[i+1]:
        ANS+=1
        if s[i]=="a":
            s[i]="b"
        else:
            s[i]="a"

print(ANS)
print("".join(s))