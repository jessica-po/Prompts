#解説参照
a = list(map(int, input().split( )))
a.sort(reverse = True)
ans = 0
ans += a[0]-a[1]
a[1]+=ans
a[2] += ans
ans += (a[0]-a[2])//2
ans += ((a[0]-a[2])%2)*2###これ
print(ans)