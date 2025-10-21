def deal(a,b,c='0'):
    if(c=='0' or a==c):
        if(a=='R'):
            return 'B'
        if(a=='B'):
            return 'R'
        if(a=='G'):
            return 'B'
    if(a=='R' and c=='B'):
        b = 'G'
    if (a == 'R' and c == 'G'):
        b = 'B'
    if (a == 'B' and c == 'R'):
        b = 'G'
    if (a == 'B' and c == 'G'):
        b = 'R'
    if (a == 'G' and c == 'B'):
        b = 'R'
    if (a == 'G' and c == 'R'):
        b = 'B'
    return b
n = int(input())
ss = input()
s = list(ss)
answer = [s[0]]
number = 0
for i in range(0,n-1):
    ans = ""
    if (s[i]==s[i+1]):
        number += 1
        if(i==n-2):
            ans = deal(s[i],s[i+1])
        else:
            ans = deal(s[i],s[i+1],s[i+2])
        s[i+1] = ans
        answer.append(ans)
    else:
        answer.append(s[i+1])
s = "".join(answer)
print(number)
print(s)