N = int(input())
al = [chr(ord('a') + i) for i in range(26)]

ans = ''
while N>0:
    N -=1
    ans += al[N%26]
    N //= 26

print(ans[::-1])