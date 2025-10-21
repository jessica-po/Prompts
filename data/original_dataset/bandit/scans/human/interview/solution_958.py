def check(s, k):
    ans = 0
    for i in range(len(s)):
        ans += abs(ord(s[i]) - ord(k[i]))
    return ans

n, k = list(map(int, input().split()))
s = input()
cnt = 0
for i in s:
    cnt += max(ord('z') - ord(i), ord(i) - ord('a'))
if k > cnt:
    print(-1)
    return
else:
    ans = ''
    cr = 0
    while k != 0:
        ps1 = ord(s[cr]) - ord('a')
        ps2 = ord('z') - ord(s[cr])
        if ps1 > k:
            ans += chr(ord(s[cr]) - k)
            k = 0
        elif ps2 > k:
            ans += chr(ord(s[cr]) + k)
            k = 0            
        else:
            if ps2 >= ps1:
                ans += 'z'
                k -= ps2
            else:
                ans += 'a'
                k -= ps1
        cr += 1
ans += s[len(ans):]
print(ans)
#print(check(ans, s))